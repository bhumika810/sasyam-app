"""English and Hindi text for the SASYAM app.

Hindi text is a draft written for this prototype. Have a Hindi-speaking
agronomist review it before farmers use it.
"""

T = {
    "en": {
        "app_title": "SASYAM",
        "app_sub": "AI-Powered Smart Agriculture Advisory System",
        "language": "Language",
        "dashboard": "Dashboard",
        "weather": "Weather",
        "crop": "Crop Advisor",
        "disease": "Disease Detection",
        "chat": "Chatbot",
        "fields": "Field Management",
        "analytics": "Analytics",
        # dashboard
        "dash_title": "Environmental monitoring",
        "take_reading": "Take a new reading",
        "soil_moisture": "Soil moisture",
        "temperature": "Temperature",
        "humidity": "Humidity",
        "soil_ph": "Soil pH",
        "moisture": "Soil moisture",
        "ph": "Soil pH",
        "status_ok": "OK",
        "status_attention": "Attention",
        "status_alert": "Alert",
        "recent_readings": "Recent readings",
        "readings_saved": "{n} of {max} readings saved",
        # weather
        "weather_title": "Weather",
        "city": "City",
        "city_placeholder": "e.g. Greater Noida",
        "get_weather": "Get current weather",
        "wind_speed": "Wind speed",
        "wind_kmh": "Wind speed (km/h)",
        "market_title": "Live mandi prices",
        "market_commodity": "Commodity",
        "market_state": "State (optional)",
        "market_get": "Get today's prices",
        "market_no_key": "To see live prices, add DATA_GOV_IN_API_KEY to your .env file (free key from data.gov.in).",
        "market_bad_key": "The data.gov.in key was rejected. Check DATA_GOV_IN_API_KEY.",
        "market_timeout": "The price service took too long. Try again.",
        "market_connection": "Could not reach the price service. Check your internet connection.",
        "market_service": "The price service did not respond as expected. Try again later.",
        "market_no_data": "No prices were published for this commodity and state today.",
        "market_note": "Prices are per quintal (100 kg), from the government daily mandi data. Check the arrival date before selling.",
        "market_best": "Highest-priced markets today",
        "market_col_market": "Market",
        "market_col_district": "District",
        "market_col_min": "Min",
        "market_col_max": "Max",
        "market_col_modal": "Modal",
        "market_col_date": "Date",
        "assistant_llm_note": "Answered with the AI assistant. Confirm any dose or spray with a local expert.",
        "season": "Season",
        "sowing": "Sowing",
        "harvest": "Harvest",
        "best_time": "Best timing",
        "crop_advice_title": "Crops for today's weather",
        "crop_advice_note": "Based on temperature and humidity only. Rainfall is not included because the current-weather data does not give it reliably. Each crop's range comes from the real dataset.",
        "st_suitable": "Suitable now",
        "st_watch": "Watch",
        "st_at_risk": "At risk",
        "reason_temperature": "Temperature {v} °C; usual range {lo}–{hi} °C",
        "reason_humidity": "Humidity {v}%; usual range {lo}–{hi}%",
        "weather_compare_note": "Weather services use different stations, so numbers can differ from Google or other apps by a few degrees or percent.",
        # crop
        "crop_title": "Crop recommendation",
        "crop_note": "Model trained on the Kaggle Crop Recommendation Dataset (22 crops).",
        "crop_missing": "The crop model is not trained yet. Run `python fetch_datasets.py`, then `python train_crop_model.py`, and restart the app.",
        "nitrogen": "Nitrogen (N)",
        "phosphorus": "Phosphorus (P)",
        "potassium": "Potassium (K)",
        "soil_ph_slider": "Soil pH",
        "temp_slider": "Temperature (°C)",
        "humidity_slider": "Humidity (%)",
        "rainfall": "Rainfall (mm)",
        "recommend": "Recommend crops",
        "recommended": "Recommended crop",
        "others": "Other possibilities",
        "accuracy": "Model accuracy on test data: {acc}%",
        "confirm_expert": "Confirm with a local agricultural expert before sowing.",
        # disease
        "disease_title": "Leaf disease check",
        "upload_leaf": "Upload a leaf photo",
        "upload_hint": "JPG, JPEG or PNG · max 5 MB",
        "uploaded_leaf": "Uploaded leaf",
        "possible_disease": "Possible disease",
        "confidence": "Confidence",
        "disease_advice": "Remove the affected leaves and check the plant every 2 days. Ask a local expert before spraying any medicine.",
        "uncertain": "The result is not clear. Please show the leaf to a local expert.",
        "no_model": "Disease check is not available yet.",
        "leaf_healthy": "The leaf looks healthy",
        "invalid_image": "The image could not be read. Please upload a clear JPG or PNG photo.",
        "cause": "Cause",
        "why_happens": "Why it happens",
        "cure_steps": "Steps to cure it",
        "cure_note": "Follow the label dose on any medicine, and confirm with a local agricultural expert before spraying.",
        # chatbot
        "chat_title": "Farm assistant",
        "chat_language": "Answer language",
        "chat_placeholder": "Ask about fertilizer, pests or irrigation",
        # fields
        "fields_title": "Field management",
        "tab_add": "Add field",
        "tab_view": "View fields",
        "field_name": "Field name",
        "crop_type": "Crop type",
        "area": "Cultivated area (acres)",
        "soil_type": "Soil type",
        "add_field": "Add field",
        "field_added": "Field '{name}' added.",
        "col_name": "Name",
        "col_crop": "Crop",
        "col_area": "Acres",
        "col_soil": "Soil",
        # analytics
        "analytics_title": "Analytics",
        "analytics_caption": "From the dashboard readings",
        "col_parameter": "Parameter",
        "col_mean": "Average",
        "col_min": "Lowest",
        "col_max": "Highest",
        "col_trend": "Change",
        "trend_view": "Trend view",
        "menu_hint": "Choose a module",
    },
    "hi": {
        "app_title": "सस्यम",
        "app_sub": "एआई आधारित स्मार्ट खेती सलाह प्रणाली",
        "language": "भाषा",
        "dashboard": "डैशबोर्ड",
        "weather": "मौसम",
        "crop": "फसल सलाह",
        "disease": "रोग पहचान",
        "chat": "खेत सहायक",
        "fields": "खेत प्रबंधन",
        "analytics": "विश्लेषण",
        "dash_title": "खेत की स्थिति",
        "take_reading": "नई रीडिंग लें",
        "soil_moisture": "मिट्टी में नमी",
        "temperature": "तापमान",
        "humidity": "नमी (आर्द्रता)",
        "soil_ph": "मिट्टी का pH",
        "moisture": "मिट्टी में नमी",
        "ph": "मिट्टी का pH",
        "status_ok": "ठीक है",
        "status_attention": "ध्यान दें",
        "status_alert": "चेतावनी",
        "recent_readings": "हाल की रीडिंग",
        "readings_saved": "{max} में से {n} रीडिंग सहेजी गईं",
        "weather_title": "मौसम की जानकारी",
        "city": "शहर",
        "city_placeholder": "जैसे ग्रेटर नोएडा",
        "get_weather": "मौसम देखें",
        "wind_speed": "हवा की गति",
        "wind_kmh": "हवा की गति (किमी/घंटा)",
        "market_title": "लाइव मंडी भाव",
        "market_commodity": "फसल",
        "market_state": "राज्य (वैकल्पिक)",
        "market_get": "आज के भाव देखें",
        "market_no_key": "लाइव भाव देखने के लिए अपनी .env फ़ाइल में DATA_GOV_IN_API_KEY जोड़ें (data.gov.in से मुफ़्त चाबी)।",
        "market_bad_key": "data.gov.in की चाबी अस्वीकार हुई। DATA_GOV_IN_API_KEY जाँचें।",
        "market_timeout": "भाव सेवा को जवाब में बहुत समय लगा। फिर से कोशिश करें।",
        "market_connection": "भाव सेवा तक नहीं पहुँच सके। इंटरनेट कनेक्शन जाँचें।",
        "market_service": "भाव सेवा ने उम्मीद के अनुसार जवाब नहीं दिया। बाद में फिर कोशिश करें।",
        "market_no_data": "इस फसल और राज्य के लिए आज कोई भाव प्रकाशित नहीं हुआ।",
        "market_note": "भाव प्रति क्विंटल (100 किलो) हैं, सरकारी दैनिक मंडी डेटा से। बेचने से पहले आगमन की तारीख देखें।",
        "market_best": "आज सबसे ऊँचे भाव वाली मंडियाँ",
        "market_col_market": "मंडी",
        "market_col_district": "ज़िला",
        "market_col_min": "न्यूनतम",
        "market_col_max": "अधिकतम",
        "market_col_modal": "मॉडल",
        "market_col_date": "तारीख",
        "assistant_llm_note": "AI सहायक से उत्तर। कोई भी खुराक या स्प्रे स्थानीय विशेषज्ञ से पुष्टि करें।",
        "season": "मौसम (सीज़न)",
        "sowing": "बुवाई",
        "harvest": "कटाई",
        "best_time": "सबसे अच्छा समय",
        "crop_advice_title": "आज के मौसम में फसलें",
        "crop_advice_note": "यह केवल तापमान और नमी पर आधारित है। बारिश शामिल नहीं है, क्योंकि मौसम डेटा में बारिश का भरोसेमंद मान नहीं मिलता। हर फसल की सीमा असली डेटासेट से ली गई है।",
        "st_suitable": "अभी उपयुक्त",
        "st_watch": "सावधान रहें",
        "st_at_risk": "खतरे में",
        "reason_temperature": "तापमान {v} °C; सामान्य सीमा {lo}–{hi} °C",
        "reason_humidity": "नमी {v}%; सामान्य सीमा {lo}–{hi}%",
        "weather_compare_note": "मौसम सेवाएँ अलग-अलग स्टेशन इस्तेमाल करती हैं, इसलिए Google या दूसरे ऐप से आँकड़े कुछ डिग्री या प्रतिशत अलग हो सकते हैं।",
        "crop_title": "फसल की सिफारिश",
        "crop_note": "मॉडल Kaggle Crop Recommendation Dataset (22 फसलें) पर प्रशिक्षित है।",
        "crop_missing": "फसल मॉडल अभी प्रशिक्षित नहीं है। `python fetch_datasets.py` और फिर `python train_crop_model.py` चलाएँ, और ऐप दोबारा शुरू करें।",
        "nitrogen": "नाइट्रोजन (N)",
        "phosphorus": "फॉस्फोरस (P)",
        "potassium": "पोटैशियम (K)",
        "soil_ph_slider": "मिट्टी का pH",
        "temp_slider": "तापमान (°C)",
        "humidity_slider": "नमी (%)",
        "rainfall": "बारिश (मिमी)",
        "recommend": "फसल सुझाएँ",
        "recommended": "सुझाई गई फसल",
        "others": "अन्य विकल्प",
        "accuracy": "परीक्षण डेटा पर मॉडल की सटीकता: {acc}%",
        "confirm_expert": "बुवाई से पहले स्थानीय कृषि विशेषज्ञ से पुष्टि करें।",
        "disease_title": "पत्ती रोग जाँच",
        "upload_leaf": "पत्ती की फोटो अपलोड करें",
        "upload_hint": "JPG, JPEG या PNG · अधिकतम 5 MB",
        "uploaded_leaf": "अपलोड की गई पत्ती",
        "possible_disease": "संभावित रोग",
        "confidence": "भरोसा",
        "disease_advice": "प्रभावित पत्तियाँ हटाएँ और हर 2 दिन में पौधे की जाँच करें। कोई दवा छिड़कने से पहले स्थानीय विशेषज्ञ से पूछें।",
        "uncertain": "परिणाम साफ़ नहीं है। कृपया पत्ती स्थानीय विशेषज्ञ को दिखाएँ।",
        "no_model": "रोग जाँच अभी उपलब्ध नहीं है।",
        "leaf_healthy": "पत्ती स्वस्थ दिखती है",
        "invalid_image": "फोटो पढ़ी नहीं जा सकी। कृपया साफ़ JPG या PNG फोटो अपलोड करें।",
        "cause": "कारण",
        "why_happens": "यह क्यों होता है",
        "cure_steps": "इलाज के कदम",
        "cure_note": "दवा लेबल की मात्रा के अनुसार ही इस्तेमाल करें, और छिड़कने से पहले स्थानीय कृषि विशेषज्ञ से पुष्टि करें।",
        "chat_title": "खेत सहायक",
        "chat_language": "उत्तर की भाषा",
        "chat_placeholder": "खाद, कीट या सिंचाई के बारे में पूछें",
        "fields_title": "खेत प्रबंधन",
        "tab_add": "नया खेत जोड़ें",
        "tab_view": "खेत देखें",
        "field_name": "खेत का नाम",
        "crop_type": "फसल",
        "area": "क्षेत्रफल (एकड़)",
        "soil_type": "मिट्टी का प्रकार",
        "add_field": "खेत जोड़ें",
        "field_added": "खेत '{name}' जोड़ा गया।",
        "col_name": "नाम",
        "col_crop": "फसल",
        "col_area": "एकड़",
        "col_soil": "मिट्टी",
        "analytics_title": "विश्लेषण",
        "analytics_caption": "डैशबोर्ड की रीडिंग से",
        "col_parameter": "मान",
        "col_mean": "औसत",
        "col_min": "सबसे कम",
        "col_max": "सबसे अधिक",
        "col_trend": "बदलाव",
        "trend_view": "रुझान",
        "menu_hint": "मॉड्यूल चुनें",
    },
}

CROP_HI = {
    "rice": "चावल", "maize": "मक्का", "chickpea": "चना", "kidneybeans": "राजमा",
    "pigeonpeas": "अरहर", "mothbeans": "मोठ", "mungbean": "मूंग", "blackgram": "उड़द",
    "lentil": "मसूर", "pomegranate": "अनार", "banana": "केला", "mango": "आम",
    "grapes": "अंगूर", "watermelon": "तरबूज", "muskmelon": "खरबूजा", "apple": "सेब",
    "orange": "संतरा", "papaya": "पपीता", "coconut": "नारियल", "cotton": "कपास",
    "jute": "जूट", "coffee": "कॉफी",
}

SOIL_HI = {"Loamy": "दोमट", "Clay": "चिकनी", "Sandy": "रेतीली", "Silt": "गाद वाली", "Black": "काली"}

WORD_HI = {"Wheat": "गेहूँ", "Rice": "धान", "Maize": "मक्का", "Cotton": "कपास", "Chickpea": "चना"}

FIELD_NAME_HI = {"North plot": "उत्तरी खेत", "River strip": "नदी किनारे का खेत", "Hill field": "पहाड़ी खेत"}

WEATHER_DESC_HI = {"scattered clouds": "बिखरे बादल", "clear sky": "साफ़ आसमान", "light rain": "हल्की बारिश"}

DISEASE_HI = {"tomato_early_blight": "टमाटर का अर्ली ब्लाइट", "rice_blast": "धान का ब्लास्ट"}
DISEASE_EN = {"tomato_early_blight": "Tomato early blight", "rice_blast": "Rice blast"}

TOPIC_KEYWORDS_HI = {
    "fertilizer": ["खाद", "उर्वरक", "यूरिया", "नाइट्रोजन"],
    "irrigation": ["सिंचाई", "पानी", "सींच"],
    "pest": ["कीट", "कीड़", "कीड़े", "छिड़काव"],
    "disease": ["रोग", "बीमारी", "धब्बे", "धब्बा", "पत्ती", "पीली"],
    "crop": ["फसल", "बोऊँ", "बोना", "उगाऊँ", "कौन सी फसल", "कौन-सी फसल"],
    "weather": ["मौसम", "बारिश", "तापमान", "नमी"],
}

TOPICS_HI_EXTRA = {
    "app_help": "मेन्यू से कोई भी पेज खोलें। डैशबोर्ड पर नई रीडिंग लें। मौसम पेज पर शहर लिखें। फसल सलाह पेज पर मान भरकर 'फसल सुझाएँ' दबाएँ। रोग पहचान पेज पर पत्ती की फोटो अपलोड करें। खेत प्रबंधन में खेत जोड़ें और सूची देखें। विश्लेषण में डैशबोर्ड रीडिंग का सारांश दिखता है।",
    "analytics": "विश्लेषण में हर रीडिंग का औसत, सबसे कम, सबसे अधिक और बदलाव दिखता है। बेहतर रुझान के लिए डैशबोर्ड पर ज़्यादा रीडिंग लें।",
    "fields": "खेत प्रबंधन में खेत का नाम, फसल, एकड़ में क्षेत्रफल और मिट्टी का प्रकार भरकर 'खेत जोड़ें' दबाएँ। 'खेत देखें' में इस सत्र में जोड़े गए सभी खेत दिखते हैं।",
    "market": "इस ऐप में आज का बाज़ार भाव नहीं दिखता। आज का भाव जानने के लिए Agmarknet (agmarknet.gov.in) या नज़दीकी मंडी देखें, और बेचने से पहले दो-तीन खरीदारों के भाव की तुलना करें।",
    "natural_fertilizer": "प्राकृतिक विकल्पों में अच्छी तरह सड़ी गोबर की खाद, कंपोस्ट, वर्मीकंपोस्ट और हरी खाद आते हैं। ये मिट्टी को समय के साथ बेहतर बनाते हैं, पर पोषक तत्व धीरे छोड़ते हैं, इसलिए बुवाई से पहले डालें। मात्रा मिट्टी जाँच की सिफ़ारिश के अनुसार रखें।",
}

TOPICS_HI = {
    "fertilizer": "मिट्टी की जाँच कराकर ही खाद डालें। नाइट्रोजन की मात्रा मौसम में कई बार में दें। ज़्यादा खाद न डालें।",
    "irrigation": "सिंचाई समय देखकर नहीं, मिट्टी की नमी देखकर करें। सुबह जल्दी सिंचाई करने से पानी कम उड़ता है।",
    "pest": "खेत की नियमित जाँच करें। पहले निगरानी करें, फिर जैविक उपाय अपनाएँ। सिर्फ़ तय सीमा पार होने पर ही स्प्रे करें।",
    "disease": "रोग पहचान पेज पर प्रभावित पत्ती की साफ़ फोटो अपलोड करें। प्रभावित पत्तियाँ हटाएँ और दवा छिड़कने से पहले स्थानीय विशेषज्ञ से पूछें।",
    "crop": "फसल सलाह पेज खोलें। मिट्टी के N, P, K, pH, तापमान, नमी और बारिश भरें। वह आपके लिए सबसे उपयुक्त फसल सुझाएगा।",
    "weather": "मौसम पेज पर शहर लिखें और 'मौसम देखें' दबाएँ। सिंचाई और छिड़काव का समय मौसम देखकर तय करें।",
}

TOPICS_HI.update(TOPICS_HI_EXTRA)
TOPIC_KEYWORDS_HI.update({
    "app_help": ["ऐप", "मेन्यू", "पेज", "कैसे खोलूँ", "कैसे इस्तेमाल", "बटन", "सेटिंग"],
    "analytics": ["विश्लेषण", "डैशबोर्ड", "रीडिंग", "औसत", "रुझान"],
    "fields": ["खेत", "खेतों", "प्लॉट", "एकड़"],
    "market": ["भाव", "बाज़ार", "मंडी", "बेचूँ", "बेच", "रेट", "खरीदार"],
    "natural_fertilizer": ["प्राकृतिक", "जैविक", "कंपोस्ट", "गोबर", "वर्मी"],
})
FALLBACK_HI = "मैं खाद, सिंचाई, कीट, रोग, फसल चुनने और मौसम के बारे में मदद कर सकता हूँ। इनमें से किसी विषय पर पूछें।"


def tr(key: str, lang: str = "en", **kw) -> str:
    text = T.get(lang, T["en"]).get(key, T["en"].get(key, key))
    return text.format(**kw) if kw else text


def crop_name(name: str, lang: str = "en") -> str:
    if lang == "hi":
        return CROP_HI.get(name.lower(), name)
    return name.capitalize()


def soil_name(name: str, lang: str = "en") -> str:
    return SOIL_HI.get(name, name) if lang == "hi" else name


def word(name: str, lang: str = "en") -> str:
    return WORD_HI.get(name, name) if lang == "hi" else name


def field_name(name: str, lang: str = "en") -> str:
    return FIELD_NAME_HI.get(name, name) if lang == "hi" else name


def weather_desc(desc: str, lang: str = "en") -> str:
    return WEATHER_DESC_HI.get(desc, desc) if lang == "hi" else desc



# Readable names for the 38 PlantVillage classes: (crop, condition) in English and Hindi.
# Hindi names are a draft for review by an agronomist.
DISEASE_NAMES = {
    'Apple___Apple_scab': ('Apple', 'Apple scab', 'सेब', 'स्कैब'),
    'Apple___Black_rot': ('Apple', 'Black rot', 'सेब', 'ब्लैक रॉट'),
    'Apple___Cedar_apple_rust': ('Apple', 'Cedar apple rust', 'सेब', 'सीडर एप्पल रस्ट'),
    'Apple___healthy': ('Apple', 'healthy', 'सेब', 'स्वस्थ'),
    'Blueberry___healthy': ('Blueberry', 'healthy', 'ब्लूबेरी', 'स्वस्थ'),
    'Cherry_(including_sour)___Powdery_mildew': ('Cherry (including sour)', 'Powdery mildew', 'चेरी', 'चूर्णिल आसिता'),
    'Cherry_(including_sour)___healthy': ('Cherry (including sour)', 'healthy', 'चेरी', 'स्वस्थ'),
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': ('Corn (maize)', 'Cercospora leaf spot Gray leaf spot', 'मक्का', 'ग्रे लीफ स्पॉट'),
    'Corn_(maize)___Common_rust_': ('Corn (maize)', 'Common rust', 'मक्का', 'सामान्य रस्ट'),
    'Corn_(maize)___Northern_Leaf_Blight': ('Corn (maize)', 'Northern Leaf Blight', 'मक्का', 'नॉर्दर्न लीफ ब्लाइट'),
    'Corn_(maize)___healthy': ('Corn (maize)', 'healthy', 'मक्का', 'स्वस्थ'),
    'Grape___Black_rot': ('Grape', 'Black rot', 'अंगूर', 'ब्लैक रॉट'),
    'Grape___Esca_(Black_Measles)': ('Grape', 'Esca (Black Measles)', 'अंगूर', 'एस्का (ब्लैक मीज़ल्स)'),
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': ('Grape', 'Leaf blight (Isariopsis Leaf Spot)', 'अंगूर', 'लीफ ब्लाइट'),
    'Grape___healthy': ('Grape', 'healthy', 'अंगूर', 'स्वस्थ'),
    'Orange___Haunglongbing_(Citrus_greening)': ('Orange', 'Haunglongbing (Citrus greening)', 'संतरा', 'ग्रीनिंग रोग'),
    'Peach___Bacterial_spot': ('Peach', 'Bacterial spot', 'आड़ू', 'बैक्टीरियल स्पॉट'),
    'Peach___healthy': ('Peach', 'healthy', 'आड़ू', 'स्वस्थ'),
    'Pepper,_bell___Bacterial_spot': ('Pepper bell', 'Bacterial spot', 'शिमला मिर्च', 'बैक्टीरियल स्पॉट'),
    'Pepper,_bell___healthy': ('Pepper bell', 'healthy', 'शिमला मिर्च', 'स्वस्थ'),
    'Potato___Early_blight': ('Potato', 'Early blight', 'आलू', 'अर्ली ब्लाइट'),
    'Potato___Late_blight': ('Potato', 'Late blight', 'आलू', 'लेट ब्लाइट'),
    'Potato___healthy': ('Potato', 'healthy', 'आलू', 'स्वस्थ'),
    'Raspberry___healthy': ('Raspberry', 'healthy', 'रसबेरी', 'स्वस्थ'),
    'Soybean___healthy': ('Soybean', 'healthy', 'सोयाबीन', 'स्वस्थ'),
    'Squash___Powdery_mildew': ('Squash', 'Powdery mildew', 'कद्दू', 'चूर्णिल आसिता'),
    'Strawberry___Leaf_scorch': ('Strawberry', 'Leaf scorch', 'स्ट्रॉबेरी', 'लीफ स्कॉर्च'),
    'Strawberry___healthy': ('Strawberry', 'healthy', 'स्ट्रॉबेरी', 'स्वस्थ'),
    'Tomato___Bacterial_spot': ('Tomato', 'Bacterial spot', 'टमाटर', 'बैक्टीरियल स्पॉट'),
    'Tomato___Early_blight': ('Tomato', 'Early blight', 'टमाटर', 'अर्ली ब्लाइट'),
    'Tomato___Late_blight': ('Tomato', 'Late blight', 'टमाटर', 'लेट ब्लाइट'),
    'Tomato___Leaf_Mold': ('Tomato', 'Leaf Mold', 'टमाटर', 'पत्ती पर फफूंद'),
    'Tomato___Septoria_leaf_spot': ('Tomato', 'Septoria leaf spot', 'टमाटर', 'सेप्टोरिया पत्ती धब्बा'),
    'Tomato___Spider_mites Two-spotted_spider_mite': ('Tomato', 'Spider mites Two-spotted spider mite', 'टमाटर', 'मकड़ी कीट'),
    'Tomato___Target_Spot': ('Tomato', 'Target Spot', 'टमाटर', 'टारगेट स्पॉट'),
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': ('Tomato', 'Tomato Yellow Leaf Curl Virus', 'टमाटर', 'पीली पत्ती मरोड़ वायरस'),
    'Tomato___Tomato_mosaic_virus': ('Tomato', 'Tomato mosaic virus', 'टमाटर', 'मोज़ेक वायरस'),
    'Tomato___healthy': ('Tomato', 'healthy', 'टमाटर', 'स्वस्थ'),
}


def disease_name(key: str, lang: str = "en") -> str:
    """Readable name for a model class, e.g. 'Tomato – Early blight' or 'टमाटर – अर्ली ब्लाइट'."""
    if key in DISEASE_NAMES:
        crop_en, cond_en, crop_hi, cond_hi = DISEASE_NAMES[key]
        return f"{crop_hi} – {cond_hi}" if lang == "hi" else f"{crop_en} – {cond_en}"
    return key


def is_healthy(key: str) -> bool:
    return key.endswith("___healthy")
