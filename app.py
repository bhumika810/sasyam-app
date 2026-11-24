"""SASYAM - AI-Powered Smart Agriculture Advisory System (prototype), English and Hindi.
Run with:  streamlit run app.py
"""
import os
import random

import streamlit as st
from dotenv import load_dotenv

import i18n as I
import logic as L


load_dotenv()

st.set_page_config(page_title="SASYAM", page_icon="🌾", layout="wide")

st.markdown("""
<style>
:root {--sy-green:#1b5e20; --sy-teal:#0f6e62; --sy-mint:#e2f0ec; --sy-line:rgba(127,127,127,0.35);}
.block-container {padding-top: 1.2rem; max-width: 1100px;}
.sasyam-title {font-size: 2rem; font-weight: 800; color: var(--sy-green); margin-bottom: 0; letter-spacing: -0.5px;}
.sasyam-sub {opacity: 0.75; margin-top: 0; margin-bottom: 1.2rem;}
[data-testid="stMetric"] {border: 1px solid var(--sy-line); border-radius: 14px; padding: 14px 16px;}
.stButton > button {border-radius: 10px; border: 1px solid var(--sy-teal); color: var(--sy-teal); font-weight: 600;}
.stButton > button:hover {background: var(--sy-mint); border-color: var(--sy-teal); color: #1e2a22;}
.stButton > button[kind="primary"] {background: var(--sy-teal); color: #fff;}
[data-testid="stForm"] {border: 1px solid var(--sy-line); border-radius: 14px; padding: 18px;}
.status-ok {color:#2e7d32; font-weight:700;}
.status-attention {color:#ef6c00; font-weight:700;}
.status-alert {color:#c62828; font-weight:700;}
h2, h3 {color: var(--sy-green);}
[data-testid="stAppDeployButton"], #MainMenu, [data-testid="stDecoration"] {display: none !important;}
</style>
""", unsafe_allow_html=True)

# ---------- session state ----------
if "rng" not in st.session_state:
    st.session_state.rng = random.Random(42)
if "history" not in st.session_state:
    st.session_state.history = []
    L.append_reading(st.session_state.history, L.simulate_reading(st.session_state.rng))  # first reading on open
if "fields" not in st.session_state:
    st.session_state.fields = []
if "chat" not in st.session_state:
    st.session_state.chat = []

LANG_CHOICES = {"English": "en", "हिन्दी": "hi"}
MODULE_KEYS = ["dashboard", "weather", "crop", "disease", "chat", "fields", "analytics"]

with st.sidebar:
    lang_label = st.radio("Language", list(LANG_CHOICES), horizontal=True, key="lang_choice")
    lang = LANG_CHOICES[lang_label]
    page = st.radio(
        "Menu",
        MODULE_KEYS,
        format_func=lambda k: f"{MODULE_KEYS.index(k) + 1}. {I.tr(k, lang)}",
        label_visibility="collapsed",
        key="menu",
    )

def _(key, **kw):
    return I.tr(key, lang, **kw)

st.markdown(f'<p class="sasyam-title">{_("app_title")}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="sasyam-sub">{_("app_sub")}</p>', unsafe_allow_html=True)


def _secret(name):
    """Read a key from Streamlit secrets when deployed (no secrets file locally is fine)."""
    try:
        return str(st.secrets.get(name, ""))
    except Exception:
        return ""


def status_label(name, value):
    s = L.status_for(name, value)  # "OK" / "Attention" / "Alert"
    code = {"OK": "status_ok", "Attention": "status_attention", "Alert": "status_alert"}[s]
    return s.lower(), _(code)


# ---------- Module 1: Dashboard ----------
if page == "dashboard":
    st.subheader(_("dash_title"))
    if st.button(_("take_reading"), type="primary"):
        L.append_reading(st.session_state.history, L.simulate_reading(st.session_state.rng))
    latest = st.session_state.history[-1]
    cols = st.columns(4)
    items = [("soil_moisture", "moisture", "%"), ("temperature", "temperature", "°C"),
             ("humidity", "humidity", "%"), ("soil_ph", "ph", "")]
    for col, (label_key, data_key, unit) in zip(cols, items):
        cls, text = status_label(data_key, latest[data_key])
        with col:
            st.metric(_(label_key), f"{latest[data_key]} {unit}".strip())
            st.markdown(f'<span class="status-{cls}">{text}</span>', unsafe_allow_html=True)
            if data_key != "ph":
                st.progress(min(max(latest[data_key] / 100, 0.0), 1.0))
    st.markdown(f"**{_('recent_readings')}**")
    st.line_chart({_("soil_moisture"): [r["moisture"] for r in st.session_state.history],
                   _("temperature"): [r["temperature"] for r in st.session_state.history],
                   _("humidity"): [r["humidity"] for r in st.session_state.history]})
    st.caption(_("readings_saved", n=len(st.session_state.history), max=L.MAX_RECORDS))

# ---------- Module 2: Weather ----------
elif page == "weather":
    st.subheader(_("weather_title"))
    city = st.text_input(_("city"), placeholder=_("city_placeholder"))
    key = os.getenv("OPENWEATHER_API_KEY", "") or _secret("OPENWEATHER_API_KEY")
    if st.button(_("get_weather")):
        result = L.fetch_weather(city, key)
        if result["ok"]:
            d = result["data"]
            c1, c2, c3 = st.columns(3)
            c1.metric(_("temperature"), f"{d['temperature']} °C")
            c2.metric(_("humidity"), f"{d['humidity']} %")
            c3.metric(_("wind_kmh"), f"{d['wind_kmh']} km/h")
            st.write(f"**{d['city']}:** {I.weather_desc(d['description'], lang)}")
        else:
            st.error(result["message"])

# ---------- Module 3: Crop Advisor ----------
elif page == "crop":
    st.subheader(_("crop_title"))
    bundle = L.load_crop_model()
    report = L.load_model_report()
    if bundle is None:
        st.warning(_("crop_missing"))
    else:
        r = bundle["ranges"]
        mid = lambda k: int((r[k][0] + r[k][1]) / 2)
        midf = lambda k: float(round((r[k][0] + r[k][1]) / 2, 1))
        c1, c2 = st.columns(2)
        vals = {}
        vals["N"] = c1.slider(_("nitrogen"), int(r["N"][0]), int(r["N"][1]), mid("N"))
        vals["P"] = c2.slider(_("phosphorus"), int(r["P"][0]), int(r["P"][1]), mid("P"))
        vals["K"] = c1.slider(_("potassium"), int(r["K"][0]), int(r["K"][1]), mid("K"))
        vals["ph"] = c2.slider(_("soil_ph_slider"), float(r["ph"][0]), float(r["ph"][1]), 6.5, step=0.01)
        vals["temperature"] = c1.slider(_("temp_slider"), float(r["temperature"][0]), float(r["temperature"][1]), midf("temperature"))
        vals["humidity"] = c2.slider(_("humidity_slider"), float(r["humidity"][0]), float(r["humidity"][1]), midf("humidity"))
        vals["rainfall"] = c1.slider(_("rainfall"), float(r["rainfall"][0]), float(r["rainfall"][1]), midf("rainfall"))
        if st.button(_("recommend"), type="primary"):
            recs = L.recommend_crops(bundle, vals, top_n=3)
            st.success(f"{_('recommended')}: **{I.crop_name(recs[0]['crop'], lang)}**")
            cal = L.load_crop_calendar().get(recs[0]["crop"])
            if cal:
                st.markdown(f"**{_('season')}:** " + (cal["season_hi"] if lang == "hi" else cal["season_en"]))
                st.markdown(f"**{_('sowing')}:** " + (cal["sow_hi"] if lang == "hi" else cal["sow_en"]))
                st.markdown(f"**{_('harvest')}:** " + (cal["harvest_hi"] if lang == "hi" else cal["harvest_en"]))
                st.markdown(f"**{_('best_time')}:** " + (cal["best_time_hi"] if lang == "hi" else cal["best_time_en"]))
            if len(recs) > 1:
                st.markdown(f"{_('others')}: " + ", ".join(I.crop_name(x["crop"], lang) for x in recs[1:]))
            st.caption(_("confirm_expert"))

# ---------- Module 4: Disease Detection ----------
elif page == "disease":
    st.subheader(_("disease_title"))
    upload = st.file_uploader(_("upload_leaf"), type=["jpg", "jpeg", "png"], help=_("upload_hint"))
    if upload is not None:
        ok, msg = L.validate_upload(upload.name, upload.size)
        if not ok:
            st.error(msg)
        else:
            st.image(upload, caption=_("uploaded_leaf"), width=320)
            result = L.classify_leaf(upload.getvalue())
            if result["status"] == "confident":
                if I.is_healthy(result["label"]):
                    st.success(_("leaf_healthy"))
                    st.write(f"{_('confidence')}: {result['confidence']*100:.0f}%")
                    kb = L.load_disease_knowledge().get(result["label"])
                    if kb:
                        for n, step in enumerate(kb["cure_hi"] if lang == "hi" else kb["cure_en"], 1):
                            st.markdown(f"{n}. {step}")
                else:
                    st.success(f"{_('possible_disease')}: **{I.disease_name(result['label'], lang)}**")
                    st.write(f"{_('confidence')}: {result['confidence']*100:.0f}%")
                    st.info(_("disease_advice"))
                    kb = L.load_disease_knowledge().get(result["label"])
                    if kb:
                        with st.expander(_("cure_steps")):
                            st.markdown(f"**{_('cause')}:** " + (kb["cause_hi"] if lang == "hi" else kb["cause_en"]))
                            st.markdown(f"**{_('why_happens')}:** " + (kb.get("why_hi", kb.get("why_en", ""))))
                            steps = kb["cure_hi"] if lang == "hi" else kb["cure_en"]
                            for n, step in enumerate(steps, 1):
                                st.markdown(f"{n}. {step}")
                            st.caption(_("cure_note"))
            elif result["status"] == "uncertain":
                st.warning(_("uncertain"))
            elif result["status"] == "invalid":
                st.error(_("invalid_image"))
            else:
                st.warning(_("no_model"))

# ---------- Module 5: Chatbot ----------
elif page == "chat":
    st.subheader(_("chat_title"))
    for role, text in st.session_state.chat:
        with st.chat_message(role):
            st.write(text)
    prompt = st.chat_input(_("chat_placeholder"))
    if prompt:
        reply = L.chatbot_reply(prompt, "Hindi" if lang == "hi" else "English")
        answer = reply["answer"]
        if reply["topic"] is None:
            ai = L.llm_answer(prompt, lang, os.getenv("ANTHROPIC_API_KEY", "") or _secret("ANTHROPIC_API_KEY") or None)
            if ai:
                answer = ai + "\n\n_" + _("assistant_llm_note") + "_"
        st.session_state.chat.append(("user", prompt))
        st.session_state.chat.append(("assistant", answer))
        st.rerun()

# ---------- Module 6: Field Management ----------
elif page == "fields":
    st.subheader(_("fields_title"))
    tab_add, tab_view = st.tabs([_("tab_add"), _("tab_view")])
    with tab_add:
        with st.form("add_field"):
            name = st.text_input(_("field_name"))
            crop = st.text_input(_("crop_type"))
            area = st.number_input(_("area"), min_value=0.0, value=1.0, step=0.5)
            soil = st.selectbox(_("soil_type"), L.SOILS, format_func=lambda s: I.soil_name(s, lang))
            submitted = st.form_submit_button(_("add_field"))
        if submitted:
            msg = L.add_field(st.session_state.fields, name, crop, area, soil)
            if "added" in msg:
                st.success(_("field_added", name=name.strip()))
            else:
                st.error(msg)
    with tab_view:
        rows = [{_("col_name"): f["name"], _("col_crop"): f["crop"], _("col_area"): f["area"],
                 _("col_soil"): I.soil_name(f["soil"], lang)} for f in st.session_state.fields]
        if rows:
            st.dataframe(rows)

# ---------- Module 7: Analytics ----------
elif page == "analytics":
    st.subheader(_("analytics_title"))
    summary = L.summarize(st.session_state.history)
    st.caption(_("analytics_caption"))
    names = {"moisture": _("moisture"), "temperature": _("temperature"), "humidity": _("humidity"), "ph": _("ph")}
    rows = [{_("col_parameter"): names[k], _("col_mean"): v["mean"], _("col_min"): v["min"],
             _("col_max"): v["max"], _("col_trend"): v["trend"]} for k, v in summary.items()]
    st.dataframe(rows)
    st.markdown(f"**{_('trend_view')}**")
    st.line_chart({_("soil_moisture"): [r["moisture"] for r in st.session_state.history],
                   _("humidity"): [r["humidity"] for r in st.session_state.history]})

    
