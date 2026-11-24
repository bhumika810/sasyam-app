"""
SASYAM prototype - core logic (no UI code here, so it can be tested).

Follows the synopsis modules:
  Module 1  environmental monitoring (simulated IoT sensors, rolling 100-record window)
  Module 2  weather intelligence (OpenWeatherMap, 5 s timeout, error handling)
  Module 3  crop recommendation (decision tree trained on the real Kaggle dataset)
  Module 4  disease detection (upload validation + confidence fallback; model optional)
  Module 5  multilingual chatbot (six languages; English fallback)
  Module 6  field management (add / view fields)
  Module 7  analytics (averages and trends)

IMPORTANT: sensor status thresholds (Module 1) are ILLUSTRATIVE placeholders.
Crop recommendations come from the real dataset, not from hand-written rules.
"""
import json
import os
import random
import statistics
from typing import Dict, List, Optional

import joblib
import pandas as pd

# ---------- Module 3: crop recommendation (real dataset) ----------
# Dataset: Kaggle "Crop Recommendation Dataset" (atharvaingle), 2,200 rows, 22 crops.
# Features: N, P, K (soil nutrients), temperature (C), humidity (%), ph, rainfall (mm).
# The model is trained by train_crop_model.py and loaded from models/crop_model.joblib.
MODEL_PATH = os.path.join("models", "crop_model.joblib")
REPORT_PATH = os.path.join("models", "crop_model_report.json")


def load_crop_model(path: str = MODEL_PATH):
    """Return the trained bundle (model, features, ranges, classes) or None if not trained yet."""
    if not os.path.exists(path):
        return None
    return joblib.load(path)


def load_model_report(path: str = REPORT_PATH) -> Optional[dict]:
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def recommend_crops(bundle: dict, values: Dict[str, float], top_n: int = 3) -> List[dict]:
    """Return the top_n crops with the model's probability for each.

    values must contain every feature in bundle['features'].
    """
    features = bundle["features"]
    missing = [f for f in features if f not in values]
    if missing:
        raise ValueError(f"Missing inputs: {missing}")
    row = pd.DataFrame([[float(values[f]) for f in features]], columns=features)
    probs = bundle["model"].predict_proba(row)[0]
    order = probs.argsort()[::-1][:top_n]
    return [{"crop": bundle["model"].classes_[i], "probability": round(float(probs[i]) * 100, 1)}
            for i in order]


# Soil types used only to describe a farmer's field (Module 6). Not a model input.
SOILS = ["Loamy", "Clay", "Sandy", "Silt", "Black"]


# ---------- Module 1: environmental monitoring ----------
MAX_RECORDS = 100  # rolling window, as in the synopsis


def simulate_reading(rng: random.Random) -> dict:
    """Simulated IoT reading: soil moisture, temperature, humidity, pH (synopsis: simulated sensors)."""
    return {
        "moisture": round(rng.uniform(15, 85), 1),
        "temperature": round(rng.uniform(12, 42), 1),
        "humidity": round(rng.uniform(30, 95), 1),
        "ph": round(rng.uniform(5.0, 8.5), 2),
    }


def append_reading(history: List[dict], reading: dict, max_records: int = MAX_RECORDS) -> List[dict]:
    """Add a reading and keep only the most recent max_records entries."""
    history.append(reading)
    if len(history) > max_records:
        del history[: len(history) - max_records]  # trim in place so the caller's list is bounded
    return history


def status_for(name: str, value: float) -> str:
    """Colour-coded status label. Thresholds are illustrative."""
    limits = {"moisture": (30, 70), "temperature": (15, 35), "humidity": (40, 85), "ph": (6.0, 7.5)}
    lo, hi = limits[name]
    if lo <= value <= hi:
        return "OK"
    margin = (hi - lo) * 0.25
    return "Attention" if (lo - margin <= value <= hi + margin) else "Alert"


# ---------- Module 2: weather intelligence ----------
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city: str, api_key: Optional[str], session=None) -> dict:
    """Return {'ok': bool, 'message': str, 'data': {...}}. Never raises on network/API errors."""
    import requests  # local import keeps the rest of the module usable without network
    if not city or not city.strip():
        return {"ok": False, "message": "Please enter a city name.", "data": None}
    if not api_key:
        return {"ok": False, "message": "No API key set. Add OPENWEATHER_API_KEY to your .env file.", "data": None}
    sess = session or requests
    query = city.strip()
    if "," not in query:
        query += ",IN"  # search India first so 'Bulandshahr' or 'Greater Noida' is not matched to another country
    try:
        resp = sess.get(WEATHER_URL, params={"q": query, "appid": api_key, "units": "metric"}, timeout=5)
    except requests.exceptions.Timeout:
        return {"ok": False, "message": "The weather service took too long to respond. Try again.", "data": None}
    except requests.exceptions.RequestException:
        return {"ok": False, "message": "Could not reach the weather service. Check your connection.", "data": None}
    if resp.status_code == 401:
        return {"ok": False, "message": "The API key was rejected. Check OPENWEATHER_API_KEY.", "data": None}
    if resp.status_code == 404:
        return {"ok": False, "message": f"City '{city}' was not found.", "data": None}
    if resp.status_code != 200:
        return {"ok": False, "message": "The weather service returned an unexpected response.", "data": None}
    try:
        body = resp.json()
        data = {
            "city": body.get("name", city),
            "temperature": body["main"]["temp"],
            "humidity": body["main"]["humidity"],
            "wind_speed": body["wind"]["speed"],
            "wind_kmh": round(body["wind"]["speed"] * 3.6, 1),
            "description": body["weather"][0]["description"],
        }
    except (ValueError, KeyError, IndexError, TypeError):
        return {"ok": False, "message": "Weather data was incomplete.", "data": None}
    return {"ok": True, "message": "OK", "data": data}


# ---------- Module 2b: weather-based crop suitability ----------
CROP_RANGES_PATH = os.path.join("models", "crop_ranges.json")


def load_crop_ranges(path: str = CROP_RANGES_PATH) -> Optional[dict]:
    """Per-crop 10th-90th percentile ranges computed from the real Kaggle dataset."""
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _factor_status(value: float, lo: float, hi: float) -> str:
    """'ok' inside the crop's observed band, 'watch' within 25% of the band width outside it, else 'risk'."""
    if lo <= value <= hi:
        return "ok"
    width = max(hi - lo, 1e-9)
    gap = lo - value if value < lo else value - hi
    return "watch" if gap <= 0.25 * width else "risk"


def weather_crop_advice(temperature: float, humidity: float, ranges: dict) -> list:
    """Judge each crop against today's temperature and humidity.

    Rainfall is not part of this check because the current-weather call does not give a
    reliable rainfall value. The result says so in the interface.
    Returns crops sorted: suitable first, then watch, then at risk.
    """
    order = {"suitable": 0, "watch": 1, "at_risk": 2}
    rows = []
    for crop, r in ranges.items():
        t = _factor_status(temperature, r["temperature"]["p10"], r["temperature"]["p90"])
        h = _factor_status(humidity, r["humidity"]["p10"], r["humidity"]["p90"])
        reasons = []
        if t != "ok":
            reasons.append(("temperature", temperature, r["temperature"]["p10"], r["temperature"]["p90"]))
        if h != "ok":
            reasons.append(("humidity", humidity, r["humidity"]["p10"], r["humidity"]["p90"]))
        if "risk" in (t, h):
            status = "at_risk"
        elif reasons:
            status = "watch"
        else:
            status = "suitable"
        rows.append({"crop": crop, "status": status, "reasons": reasons})
    rows.sort(key=lambda x: (order[x["status"]], x["crop"]))
    return rows


# ---------- Module 4: disease detection ----------
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}
MAX_UPLOAD_BYTES = 5 * 1024 * 1024
CONFIDENCE_THRESHOLD = 0.60  # below this the result is reported as uncertain
DISEASE_MODEL_PATH = os.path.join("models", "disease_model.keras")
DISEASE_CLASSES_PATH = os.path.join("models", "disease_classes.json")
DISEASE_REPORT_PATH = os.path.join("models", "disease_model_report.json")
DISEASE_IMAGE_SIZE = 64  # must match train_disease_model.py
_disease_cache = {}


def validate_upload(filename: str, size_bytes: int):
    """Return (ok, message). Checks format and size before any analysis."""
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if ext not in ALLOWED_EXTENSIONS:
        return False, "Please upload a JPG, JPEG or PNG image."
    if size_bytes <= 0:
        return False, "The uploaded file is empty."
    if size_bytes > MAX_UPLOAD_BYTES:
        return False, "The image is larger than 5 MB. Please upload a smaller file."
    return True, "Image accepted."


def interpret_prediction(label: str, confidence: float, threshold: float = CONFIDENCE_THRESHOLD) -> dict:
    """Low confidence is reported as uncertain and a second opinion is advised."""
    if confidence < threshold:
        return {"status": "uncertain", "label": label, "confidence": confidence,
                "message": "The result is uncertain. Please seek a second opinion from a local expert."}
    return {"status": "confident", "label": label, "confidence": confidence,
            "message": "General guidance only. Confirm with a local agricultural expert before treatment."}


def load_disease_model():
    """Return (keras_model, class_names) or None if the model has not been trained."""
    if "pair" in _disease_cache:
        return _disease_cache["pair"]
    if not os.path.exists(DISEASE_MODEL_PATH) or not os.path.exists(DISEASE_CLASSES_PATH):
        return None
    import tensorflow as tf  # imported only when the model is actually used
    with open(DISEASE_CLASSES_PATH, encoding="utf-8") as f:
        classes = json.load(f)
    pair = (tf.keras.models.load_model(DISEASE_MODEL_PATH), classes)
    _disease_cache["pair"] = pair
    return pair


DISEASE_KNOWLEDGE_PATH = os.path.join("models", "disease_knowledge.json")


def load_disease_knowledge(path: str = DISEASE_KNOWLEDGE_PATH) -> dict:
    """Cause, reason and cure steps for each disease class (English and Hindi)."""
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_crop_calendar(path: str = os.path.join("models", "crop_calendar.json")) -> dict:
    """Season, sowing and harvest windows for each crop (general guide, check locally)."""
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_disease_report():
    if not os.path.exists(DISEASE_REPORT_PATH):
        return None
    with open(DISEASE_REPORT_PATH, encoding="utf-8") as f:
        return json.load(f)


def predict_leaf(image_bytes: bytes, pair) -> dict:
    """Run the trained classifier on uploaded image bytes."""
    import io
    import numpy as np
    from PIL import Image
    model, classes = pair
    with Image.open(io.BytesIO(image_bytes)) as im:
        im = im.convert("RGB").resize((DISEASE_IMAGE_SIZE, DISEASE_IMAGE_SIZE), Image.BILINEAR)
        arr = np.asarray(im, dtype=np.float32)[None, ...]
    probs = model.predict(arr, verbose=0)[0]
    idx = int(np.argmax(probs))
    return interpret_prediction(classes[idx], float(probs[idx]))


def classify_leaf(image_bytes: bytes, model=None) -> dict:
    """Classify a leaf photo.

    model=None uses the trained model in models/ if it exists. A callable model
    (image bytes -> (label, confidence)) can be passed for testing or for another model.
    """
    if model is not None:
        label, confidence = model(image_bytes)
        return interpret_prediction(label, confidence)
    pair = load_disease_model()
    if pair is None:
        return {"status": "no_model", "message": "The disease model is not trained yet."}
    try:
        return predict_leaf(image_bytes, pair)
    except Exception:
        return {"status": "invalid", "message": "The image could not be read. Please upload a clear JPG or PNG photo."}


# ---------- Module 5: multilingual chatbot ----------
import i18n as _i18n

LANGUAGES = ["English", "Hindi", "Marathi", "Gujarati", "Tamil", "Telugu"]
_LANG_CODE = {"English": "en", "Hindi": "hi"}  # languages with reviewed translations

# English answers (illustrative guidance only).
TOPICS = {
    "fertilizer": "Test your soil before applying fertilizer, and split nitrogen doses across the season. Avoid over-application.",
    "irrigation": "Irrigate based on soil moisture rather than a fixed schedule. Water early in the morning to reduce evaporation.",
    "pest": "Scout your field regularly. Use integrated pest management: monitor first, use biological control where possible, and spray only when thresholds are crossed.",
    "disease": "Open Disease Detection and upload a clear photo of the affected leaf. Remove badly affected leaves, and ask a local expert before spraying any medicine.",
    "crop": "Open the Crop Advisor and enter nitrogen, phosphorus, potassium, soil pH, temperature, humidity and rainfall. It suggests the most suitable crop for those conditions.",
    "weather": "Open the Weather page, type your city and press Get current weather. Plan irrigation and spraying around the forecast.",
    "app_help": "Use the menu on the left to open each page. Dashboard: take a reading. Weather: type a city. Crop Advisor: set the values and press Recommend. Disease Detection: upload a leaf photo. Field Management: add a field and view the list. Analytics: summary of your dashboard readings.",
    "analytics": "Analytics shows the average, lowest, highest and change for each dashboard reading. Take more readings on the Dashboard to see a clearer trend.",
    "fields": "In Field Management, enter the field name, crop, area in acres and soil type, then press Add field. View fields shows all the fields you added in this session.",
    "market": "This app does not show live market prices. For today's price, check Agmarknet (agmarknet.gov.in) or your nearest mandi, and compare two or three buyers before selling.",
    "natural_fertilizer": "Natural options include well-rotted farmyard manure, compost, vermicompost and green manure. They improve soil over time, but release nutrients slowly, so apply them before sowing. Apply the amount your soil test recommends.",
}
TOPIC_KEYWORDS = {
    "fertilizer": ["fertilizer", "fertiliser", "urea", "nitrogen", "manure", "nutrient"],
    "irrigation": ["irrigation", "water", "watering", "irrigate"],
    "pest": ["pest", "insect", "worm", "bug", "spray"],
    "disease": ["disease", "blight", "spot", "rust", "yellow", "leaf", "mold", "mildew"],
    "crop": ["crop", "sow", "grow", "which crop", "plant"],
    "weather": ["weather", "forecast", "temperature", "rain", "humidity"],
    "app_help": ["app", "menu", "page", "how to use", "how do i use", "button", "setting", "how to open"],
    "analytics": ["analytics", "dashboard", "reading", "average", "trend graph"],
    "fields": ["field", "fields", "plot", "acre"],
    "market": ["price", "market", "mandi", "sell", "rate", "buyer"],
    "natural_fertilizer": ["natural", "organic", "compost", "manure", "vermicompost"],
}
FALLBACK_EN = ("I can help with fertilizer, irrigation, pests, diseases, choosing a crop and the weather. "
               "Try asking about one of these.")


FERT_WORDS = ["fertiliz", "fertilis", "manure", "compost", "urea", "dap", "npk", "natural", "chemical",
              "खाद", "उर्वरक", "गोबर", "कंपोस्ट", "यूरिया", "प्राकृतिक", "रासायनिक"]


def _kb_matches(query: str, lang_code: str, max_hits: int = 3) -> list:
    """Knowledge-base entries that match, best first. A second entry is kept when it is
    nearly as strong, so mixed questions such as 'natural and chemical fertilizer for maize'
    get both answers."""
    import knowledge_base as KBM
    q_en = (query or "").lower()
    q_hi = query or ""
    has_devanagari = any(0x900 <= ord(ch) <= 0x97F for ch in q_hi)
    scored = []
    for entry in KBM.KB:
        score = sum(len(kw) for kw in entry["kw_en"] if kw in q_en)
        if lang_code == "hi" or has_devanagari:
            score += sum(len(kw) for kw in entry["kw_hi"] if kw in q_hi)
        if score > 0 and entry["id"].startswith("fert_crop_") and any(w in q_en or w in q_hi for w in FERT_WORDS):
            score += 12  # a named crop in a fertilizer question should win over generic entries
        if score > 0:
            scored.append((score, entry))
    scored.sort(key=lambda t: t[0], reverse=True)
    if not scored:
        return []
    top = scored[0][0]
    return [e for sc, e in scored[:max_hits] if sc >= 0.2 * top]


def llm_answer(query: str, lang_code: str, api_key: Optional[str], session=None) -> Optional[str]:
    """Optional: answer questions outside the knowledge base with the Anthropic API.

    Needs ANTHROPIC_API_KEY in .env (or hosting secrets). Returns None if no key or on any error.
    """
    if not api_key:
        return None
    sess = session or requests
    system = ("You are the farm assistant inside SASYAM, an app for Indian farmers. Answer briefly and practically. "
              "Always tell the farmer to confirm fertilizer or spray doses with a soil test, the product label "
              "and a local agricultural officer. Answer in " + ("Hindi (Devanagari script)" if lang_code == "hi" else "English") + ".")
    try:
        resp = sess.post("https://api.anthropic.com/v1/messages",
                         headers={"x-api-key": api_key, "anthropic-version": "2023-06-01", "content-type": "application/json"},
                         json={"model": "claude-haiku-5-5", "max_tokens": 400, "system": system,
                               "messages": [{"role": "user", "content": query}]},
                         timeout=20)
        if resp.status_code != 200:
            return None
        parts = resp.json().get("content", [])
        text = " ".join(p.get("text", "") for p in parts if p.get("type") == "text").strip()
        return text or None
    except Exception:
        return None


def chatbot_reply(query: str, language: str = "English") -> dict:
    """Keyword-based answer in English or Hindi. Other languages fall back to English with a note."""
    if language not in LANGUAGES:
        language = "English"
    code = _LANG_CODE.get(language)
    matches = _kb_matches(query, code or "en")
    if matches:
        parts = [e["hi"] if code == "hi" else e["en"] for e in matches]
        note = None
        if code is None:
            note = (f"{language} translation is not yet available in this prototype; "
                    "showing the English answer. Translations must be reviewed by subject experts.")
        return {"answer": "\n\n".join(parts), "topic": matches[0]["id"], "language": language, "note": note}
    q = (query or "").lower()
    topic = None
    for t, words in TOPIC_KEYWORDS.items():
        if any(w in q for w in words):
            topic = t
            break
    if topic is None and code == "hi":
        for t, words in _i18n.TOPIC_KEYWORDS_HI.items():
            if any(w in query for w in words):
                topic = t
                break
    if code == "hi":
        answer = _i18n.TOPICS_HI[topic] if topic else _i18n.FALLBACK_HI
        return {"answer": answer, "topic": topic, "language": language, "note": None}
    answer = TOPICS[topic] if topic else FALLBACK_EN
    note = None
    if code is None:
        note = (f"{language} translation is not yet available in this prototype; "
                "showing the English answer. Translations must be reviewed by subject experts.")
    return {"answer": answer, "topic": topic, "language": language, "note": note}


# ---------- Module 6: field management ----------
def add_field(fields: List[dict], name: str, crop: str, area: float, soil: str) -> str:
    """Validate and add a field. Returns a message string."""
    if not name or not name.strip():
        return "Field name is required."
    if area is None or area <= 0:
        return "Cultivated area must be greater than zero."
    if soil not in SOILS:
        return "Please choose a valid soil type."
    if any(f["name"].lower() == name.strip().lower() for f in fields):
        return f"A field named '{name.strip()}' already exists."
    fields.append({"name": name.strip(), "crop": crop, "area": float(area), "soil": soil})
    return f"Field '{name.strip()}' added."


# ---------- Module 7: analytics ----------
def summarize(history: List[dict]) -> dict:
    """Average values and the trend (last value minus first) for each recorded parameter."""
    if not history:
        return {}
    out = {}
    for key in ["moisture", "temperature", "humidity", "ph"]:
        values = [r[key] for r in history]
        out[key] = {
            "mean": round(statistics.mean(values), 2),
            "min": min(values),
            "max": max(values),
            "trend": round(values[-1] - values[0], 2),
        }
    return out
