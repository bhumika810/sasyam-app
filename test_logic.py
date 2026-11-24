"""Run with:  python test_logic.py   (or: python -m pytest -q)

Crop-model tests use a GENERATED file with the same columns as the real dataset, only to check
the code path. They do not measure the real dataset's accuracy; use train_crop_model.py for that.
"""
import inspect
import json
import os
import random
import sys
import tempfile

import requests

import logic as L
import train_crop_model as T


def make_test_csv(path, rows_per_class=30, seed=0):
    rng = random.Random(seed)
    names = ["rice", "maize", "chickpea", "cotton"]
    lines = ["N,P,K,temperature,humidity,ph,rainfall,label"]
    for i, name in enumerate(names):
        for _ in range(rows_per_class):
            vals = [40 + 30 * i + rng.uniform(-5, 5), 30 + 10 * i + rng.uniform(-3, 3),
                    20 + 5 * i + rng.uniform(-2, 2), 20 + 4 * i + rng.uniform(-1, 1),
                    50 + 5 * i + rng.uniform(-3, 3), 6.0 + 0.3 * i + rng.uniform(-0.1, 0.1),
                    80 + 40 * i + rng.uniform(-5, 5)]
            lines.append(",".join(f"{v:.2f}" for v in vals) + f",{name}")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def test_training_produces_model_and_report():
    d = tempfile.mkdtemp()
    csv = os.path.join(d, "test_synthetic.csv")
    make_test_csv(csv)
    report = T.train(csv, os.path.join(d, "m.joblib"), os.path.join(d, "r.json"))
    assert report["rows"] == 120 and report["classes"] == 4
    assert 0 <= report["holdout_test_accuracy"] <= 1
    assert json.load(open(os.path.join(d, "r.json")))["rows"] == 120


def test_recommend_from_trained_bundle():
    d = tempfile.mkdtemp()
    csv = os.path.join(d, "test_synthetic.csv")
    make_test_csv(csv)
    T.train(csv, os.path.join(d, "m.joblib"), os.path.join(d, "r.json"))
    bundle = L.load_crop_model(os.path.join(d, "m.joblib"))
    values = {f: sum(bundle["ranges"][f]) / 2 for f in bundle["features"]}
    recs = L.recommend_crops(bundle, values, top_n=3)
    assert len(recs) == 3
    probs = [r["probability"] for r in recs]
    assert probs == sorted(probs, reverse=True)
    assert all(0 <= p <= 100 for p in probs)


def test_missing_input_is_rejected():
    d = tempfile.mkdtemp()
    csv = os.path.join(d, "test_synthetic.csv")
    make_test_csv(csv)
    T.train(csv, os.path.join(d, "m.joblib"), os.path.join(d, "r.json"))
    bundle = L.load_crop_model(os.path.join(d, "m.joblib"))
    try:
        L.recommend_crops(bundle, {"N": 1})
        assert False, "expected ValueError"
    except ValueError:
        pass


def test_training_summary_fields_are_present():
    assert callable(L.load_disease_model) and L.DISEASE_IMAGE_SIZE == 64


def test_no_model_returns_none():
    assert L.load_crop_model(os.path.join(tempfile.mkdtemp(), "missing.joblib")) is None


def test_training_rejects_bad_csv():
    d = tempfile.mkdtemp()
    bad = os.path.join(d, "bad.csv")
    with open(bad, "w") as f:
        f.write("N,P,label\n1,2,rice\n")
    try:
        T.train(bad, os.path.join(d, "m.joblib"), os.path.join(d, "r.json"))
        assert False, "expected ValueError"
    except ValueError as e:
        assert "missing columns" in str(e)


def test_rolling_window_keeps_last_100():
    h = []
    rng = random.Random(1)
    for _ in range(150):
        L.append_reading(h, L.simulate_reading(rng))
    assert len(h) == 100


def test_status_labels():
    assert L.status_for("moisture", 50) == "OK"
    assert L.status_for("moisture", 5) == "Alert"


class FakeResp:
    def __init__(self, code, body=None):
        self.status_code, self._body = code, body
    def json(self):
        if self._body is None:
            raise ValueError("no json")
        return self._body


class FakeSession:
    def __init__(self, resp=None, exc=None):
        self.resp, self.exc = resp, exc
    def get(self, *a, **k):
        if self.exc:
            raise self.exc
        return self.resp


GOOD = {"name": "Noida", "main": {"temp": 30.5, "humidity": 60}, "wind": {"speed": 3.2},
        "weather": [{"description": "clear sky"}]}


def test_weather_success():
    r = L.fetch_weather("Noida", "k", session=FakeSession(FakeResp(200, GOOD)))
    assert r["ok"] and r["data"]["temperature"] == 30.5


def test_weather_errors():
    assert "rejected" in L.fetch_weather("Noida", "bad", session=FakeSession(FakeResp(401)))["message"]
    assert "not found" in L.fetch_weather("Zzz", "k", session=FakeSession(FakeResp(404)))["message"]
    assert "too long" in L.fetch_weather("Noida", "k", session=FakeSession(exc=requests.exceptions.Timeout()))["message"]
    assert "connection" in L.fetch_weather("Noida", "k", session=FakeSession(exc=requests.exceptions.ConnectionError()))["message"]
    assert "API key" in L.fetch_weather("Noida", "", session=FakeSession(FakeResp(200, GOOD)))["message"]


def test_upload_validation():
    assert L.validate_upload("leaf.JPG", 1000)[0]
    assert not L.validate_upload("leaf.gif", 1000)[0]
    assert not L.validate_upload("leaf.png", 6 * 1024 * 1024)[0]


def test_low_confidence_is_uncertain():
    assert L.interpret_prediction("Rust", 0.4)["status"] == "uncertain"
    assert L.interpret_prediction("Rust", 0.9)["status"] == "confident"


def test_invalid_image_is_handled_not_crashed():
    assert L.classify_leaf(b"not an image")["status"] in ("no_model", "invalid")


def test_fake_model_result_is_used():
    r = L.classify_leaf(b"x", model=lambda b: ("Tomato___Early_blight", 0.9))
    assert r["status"] == "confident" and r["label"] == "Tomato___Early_blight"
    assert L.classify_leaf(b"x", model=lambda b: ("Tomato___Early_blight", 0.3))["status"] == "uncertain"


def test_disease_names_and_healthy_flag():
    import i18n as I
    assert I.disease_name("Tomato___Early_blight", "en") == "Tomato – Early blight"
    assert I.disease_name("Tomato___Early_blight", "hi") == "टमाटर – अर्ली ब्लाइट"
    assert I.is_healthy("Apple___healthy") and not I.is_healthy("Apple___Black_rot")


def test_chatbot_topics_and_fallback():
    assert L.chatbot_reply("when to irrigate my wheat")["topic"] == "irrigation"
    r = L.chatbot_reply("खाद कितनी डालूँ", "Hindi")
    assert r["topic"].startswith("fert") and r["note"] is None
    m = L.chatbot_reply("fertilizer dose", "Marathi")
    assert m["note"] is not None
    assert L.chatbot_reply("hello")["topic"] is None


def test_field_management():
    f = []
    assert "added" in L.add_field(f, "North plot", "Wheat", 2, "Loamy")
    assert "already exists" in L.add_field(f, "north plot", "Wheat", 2, "Loamy")
    assert "greater than zero" in L.add_field(f, "B", "Rice", 0, "Clay")


def test_weather_crop_advice_flags_crops():
    ranges = L.load_crop_ranges()
    if ranges is None:
        return
    rows = L.weather_crop_advice(27.4, 58, ranges)
    statuses = {r["crop"]: r["status"] for r in rows}
    assert set(statuses.values()) <= {"suitable", "watch", "at_risk"}
    assert statuses["apple"] == "at_risk"          # apple needs cool, humid conditions
    assert rows[0]["status"] == "suitable"          # suitable crops are listed first


def test_wind_converted_to_kmh():
    body = {"name": "Bulandshahr", "main": {"temp": 25, "humidity": 50}, "wind": {"speed": 3.0},
            "weather": [{"description": "haze"}]}
    r = L.fetch_weather("Bulandshahr", "k", session=FakeSession(FakeResp(200, body)))
    assert r["data"]["wind_kmh"] == 10.8


def test_market_module_handles_success_and_errors():
    import market as M
    ok = {"records": [{"commodity": "Maize", "market": "Khurja", "district": "Bulandshahr", "state": "Uttar Pradesh",
                       "arrival_date": "24/11/2026", "min_price": "1800", "max_price": "2100", "modal_price": "2000"},
                      {"commodity": "Maize", "market": "Noida", "district": "Gautam Buddha Nagar", "state": "Uttar Pradesh",
                       "arrival_date": "24/11/2026", "min_price": "1900", "max_price": "2200", "modal_price": "2150"}]}
    r = M.fetch_mandi_prices("Maize", "Uttar Pradesh", "k", session=FakeSession(FakeResp(200, ok)))
    assert r["ok"] and r["rows"][0]["market"] == "Noida"          # highest modal price first
    mixed = {"records": [{"commodity": "Snakeguard", "market": "X", "modal_price": 3800, "min_price": 1, "max_price": 2, "arrival_date": "d", "district": "", "state": ""},
                         {"commodity": "Maize", "market": "Y", "modal_price": 2100, "min_price": 1, "max_price": 2, "arrival_date": "d", "district": "", "state": ""}]}
    assert M.fetch_mandi_prices("maize", "", "k", session=FakeSession(FakeResp(200, mixed)))["rows"][0]["market"] == "Y"
    assert M.fetch_mandi_prices("Maize", "", "k", session=FakeSession(FakeResp(403)))["message"] == "bad_key"
    assert M.fetch_mandi_prices("Maize", "", None)["message"] == "no_key"
    assert M.fetch_mandi_prices("Maize", "", "k", session=FakeSession(exc=requests.exceptions.Timeout()))["message"] == "timeout"


def test_knowledge_base_routes_questions():
    cases = {"which fertilizer for my maize, natural and chemical?": "fert_chemical",
             "price of maize in mandi": "market_prices",
             "how do I add a field": "fields",
             "startup idea with banana": "startup_ideas",
             "when to irrigate my wheat": "irrigation"}
    for q, expected in cases.items():
        assert L.chatbot_reply(q, "English")["topic"] == expected, q
    assert L.chatbot_reply("hello", "English")["topic"] is None


def test_disease_knowledge_covers_all_classes():
    kb = L.load_disease_knowledge()
    classes = json.load(open(os.path.join("models", "disease_classes.json"), encoding="utf-8")) if os.path.exists(os.path.join("models", "disease_classes.json")) else []
    if classes:
        assert all(c in kb for c in classes)
        assert all(kb[c].get("why_hi") for c in classes)


def test_summary():
    h = [{"moisture": 40, "temperature": 20, "humidity": 50, "ph": 6.5},
         {"moisture": 60, "temperature": 24, "humidity": 70, "ph": 7.0}]
    s = L.summarize(h)
    assert s["moisture"]["mean"] == 50 and s["moisture"]["trend"] == 20


if __name__ == "__main__":
    fails = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_") and inspect.isfunction(fn):
            try:
                fn(); print("PASS", name)
            except Exception as e:
                fails += 1; print("FAIL", name, repr(e))
    sys.exit(1 if fails else 0)
