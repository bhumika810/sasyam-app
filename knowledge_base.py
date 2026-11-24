"""Farm assistant knowledge base (English and Hindi).

Each entry: id, keywords (English and Hindi), answer (English and Hindi).
Quantities are typical ranges for general guidance. Every fertilizer or spray answer tells the
farmer to follow a soil test and the product label, and to confirm with a local agricultural officer.
"""

KB = [
 {"id": "app_overview", "kw_en": ["app", "sasyam", "what is this", "what can you do", "help", "menu", "pages"],
  "kw_hi": ["ऐप", "सस्यम", "क्या है", "क्या कर", "मदद", "मेन्यू", "पेज"],
  "en": "SASYAM has seven pages: Dashboard (sensor readings), Weather (current weather and crop suitability), Crop Advisor (best crop from soil and climate values), Disease Detection (leaf photo check with cure steps), Farm assistant (this chat), Field Management (your fields), and Analytics (summary of readings and market prices). Use the menu on the left to open a page, and the switch at the top to change language.",
  "hi": "सस्यम में सात पेज हैं: डैशबोर्ड (सेंसर रीडिंग), मौसम (आज का मौसम और फसल की स्थिति), फसल सलाह (मिट्टी और जलवायु से सबसे उपयुक्त फसल), रोग पहचान (पत्ती की फोटो से रोग और इलाज), खेत सहायक (यह चैट), खेत प्रबंधन (आपके खेत), और विश्लेषण (रीडिंग का सारांश और बाज़ार भाव)। बाईं ओर के मेन्यू से पेज खोलें और ऊपर के स्विच से भाषा बदलें।"},

 {"id": "dashboard", "kw_en": ["dashboard", "reading", "sensor", "moisture", "ph reading", "status", "ok", "attention", "alert", "take reading"],
  "kw_hi": ["डैशबोर्ड", "रीडिंग", "सेंसर", "नमी", "स्थिति", "चेतावनी", "नई रीडिंग"],
  "en": "The Dashboard shows four readings: soil moisture, temperature, humidity and soil pH. Press 'Take a new reading' to add one. Each card shows OK, Attention or Alert based on fixed limits. Readings in this prototype are simulated, not from real sensors. The app keeps the latest 100 readings and shows them in the chart.",
  "hi": "डैशबोर्ड पर चार रीडिंग दिखती हैं: मिट्टी की नमी, तापमान, नमी (आर्द्रता) और मिट्टी का pH। नई रीडिंग के लिए 'नई रीडिंग लें' दबाएँ। हर कार्ड पर तय सीमा के आधार पर ठीक है, ध्यान दें या चेतावनी दिखती है। इस प्रोटोटाइप में रीडिंग नकली (सिमुलेटेड) हैं, असली सेंसर से नहीं। ऐप नवीनतम 100 रीडिंग रखता है और चार्ट में दिखाता है।"},

 {"id": "analytics", "kw_en": ["analytics", "average", "mean", "lowest", "highest", "change", "trend", "summary", "statistics"],
  "kw_hi": ["विश्लेषण", "औसत", "सबसे कम", "सबसे अधिक", "बदलाव", "रुझान", "सारांश"],
  "en": "Analytics shows the average, lowest, highest and change for each dashboard reading, plus a trend chart. 'Change' is the difference between the first and the latest reading in the list. Take more readings on the Dashboard for a clearer trend. The market price section on this page shows live mandi prices when a data.gov.in key is set.",
  "hi": "विश्लेषण में हर डैशबोर्ड रीडिंग का औसत, सबसे कम, सबसे अधिक और बदलाव दिखता है, साथ में रुझान का चार्ट। 'बदलाव' पहली और नवीनतम रीडिंग का अंतर है। साफ़ रुझान के लिए डैशबोर्ड पर ज़्यादा रीडिंग लें। इस पेज पर बाज़ार भाव भी है, जो data.gov.in की चाबी डालने पर लाइव दिखता है।"},

 {"id": "weather", "kw_en": ["weather", "forecast", "humidity", "wind", "city", "temperature today", "rain today"],
  "kw_hi": ["मौसम", "हवा", "शहर", "आज का तापमान", "आज बारिश"],
  "en": "Type a city on the Weather page and press 'Get current weather'. You see temperature, humidity and wind in m/s and km/h. The city is searched in India first, so Bulandshahr or Greater Noida is matched correctly.",
  "hi": "मौसम पेज पर शहर लिखकर 'मौसम देखें' दबाएँ। तापमान, नमी और हवा m/s व किमी/घंटा में दिखते हैं। शहर पहले भारत में खोजा जाता है, इसलिए बुलंदशहर या ग्रेटर नोएडा सही मिलते हैं।"},

 {"id": "crop_advisor", "kw_en": ["crop advisor", "recommend", "which crop", "best crop", "suggest crop", "nitrogen", "soil values", "crop suggestion"],
  "kw_hi": ["फसल सलाह", "फसल सुझाव", "कौन सी फसल", "सबसे अच्छी फसल", "नाइट्रोजन", "मिट्टी के मान"],
  "en": "Crop Advisor takes seven values: nitrogen, phosphorus and potassium from a soil test, soil pH, temperature, humidity and rainfall. It uses a decision tree trained on 2,200 real records of 22 crops and shows the top crop with the other likely options. The app shows the model's measured accuracy (about 96 percent on held-out data). Use the result with your soil test and local advice.",
  "hi": "फसल सलाह सात मान लेती है: मिट्टी जाँच से नाइट्रोजन, फॉस्फोरस और पोटैशियम, मिट्टी का pH, तापमान, नमी और बारिश। यह 22 फसलों के 2,200 असली रिकॉर्ड पर सिखाए गए निर्णय-वृक्ष (डिसीज़न ट्री) से सबसे उपयुक्त फसल बताती है, साथ में अन्य संभावित विकल्प भी। मॉडल की मापी गई सटीकता लगभग 96 प्रतिशत है। नतीजे को अपनी मिट्टी जाँच और स्थानीय सलाह के साथ इस्तेमाल करें।"},

 {"id": "crop_timing", "kw_en": ["when to sow", "sowing", "season", "harvest", "when to grow", "best time", "sowing time", "which month"],
  "kw_hi": ["कब बोएँ", "बुवाई", "मौसम", "कटाई", "कब उगाएँ", "सबसे अच्छा समय", "कौन सा महीना"],
  "en": "After a recommendation, Crop Advisor shows the season (kharif, rabi or zaid), the sowing window, the harvest window and the best timing for that crop. Sowing dates are general guides for the main growing regions. Your local Krishi Vigyan Kendra or agricultural officer can confirm the right date for your district.",
  "hi": "फसल सुझाव के बाद फसल सलाह पर सीज़न (खरीफ, रबी या ज़ायद), बुवाई का समय, कटाई का समय और उस फसल का सबसे अच्छा समय दिखता है। बुवाई की तारीखें मुख्य क्षेत्रों के लिए सामान्य मार्गदर्शन हैं। अपने ज़िले की सही तारीख के लिए नज़दीकी कृषि विज्ञान केंद्र (KVK) या कृषि अधिकारी से पूछें।"},

 {"id": "disease_check", "kw_en": ["disease", "leaf", "photo", "upload", "spots", "yellow leaves", "blight", "rust", "mildew", "identify disease"],
  "kw_hi": ["रोग", "पत्ती", "फोटो", "अपलोड", "धब्बे", "पीली पत्ती", "झुलसा", "रस्ट", "चूर्णिल"],
  "en": "On Disease Detection, upload a clear JPG or PNG photo of one leaf in good light. The app names the disease with its confidence, then shows the cause, why it happens and the cure steps. Results below 60 percent confidence are marked uncertain, and you should show the leaf to a local expert. The model was trained on controlled photos, so field photos may give lower accuracy.",
  "hi": "रोग पहचान पेज पर अच्छी रोशनी में एक पत्ती की साफ़ JPG या PNG फोटो अपलोड करें। ऐप रोग का नाम और भरोसा बताएगा, फिर कारण, यह क्यों होता है, और इलाज के कदम दिखाएगा। 60 प्रतिशत से कम भरोसे वाले नतीजे 'अनिश्चित' माने जाते हैं, तब पत्ती स्थानीय विशेषज्ञ को दिखाएँ। मॉडल नियंत्रित फोटो पर सिखाया गया है, इसलिए खेत की फोटो पर सटीकता कम हो सकती है।"},

 {"id": "disease_cure", "kw_en": ["cure", "treat", "treatment", "how to cure", "remove leaves", "spray for disease", "what should i do disease", "my crop has disease"],
  "kw_hi": ["इलाज", "उपचार", "कैसे ठीक", "दवा", "फसल में रोग", "क्या करूँ"],
  "en": "General steps for most leaf diseases: 1) Remove and destroy badly infected leaves or plants. 2) Improve air flow and water at the base in the morning. 3) Keep the crop well fed so it can recover. 4) If the disease spreads, spray a fungicide or bactericide recommended for that crop, using the label dose and the spray schedule on the label. 5) Repeat only as the label says, and rotate with a different crop next season. Virus diseases have no cure: remove the plant and control the insects that spread them.",
  "hi": "ज़्यादातर पत्ती रोगों के लिए सामान्य कदम: 1) बुरी तरह संक्रमित पत्तियाँ या पौधे हटाकर नष्ट करें। 2) हवा का बहाव सुधारें और सुबह जड़ में पानी दें। 3) फसल को सही खाद दें ताकि वह ठीक हो सके। 4) रोग फैले तो उस फसल के लिए अनुमोदित फफूंदनाशक या बैक्टीरियानाशक लेबल की मात्रा में छिड़कें। 5) दोबारा छिड़काव लेबल के अनुसार ही करें और अगले सीज़न में फसल बदलें। वायरस रोगों का इलाज नहीं है: पौधा हटाएँ और उन्हें फैलाने वाले कीटों को नियंत्रित करें।"},

 {"id": "fert_natural", "kw_en": ["natural fertilizer", "organic", "compost", "manure", "vermicompost", "farmyard", "green manure", "neem cake", "natural"],
  "kw_hi": ["प्राकृतिक खाद", "जैविक", "कंपोस्ट", "गोबर", "वर्मीकंपोस्ट", "हरी खाद", "नीम खली", "प्राकृतिक"],
  "en": "Natural fertilizers: well-rotted farmyard manure (about 8–10 tonnes per hectare before sowing), compost or vermicompost (2–3 tonnes per hectare), green manure such as dhaincha or sunnhemp ploughed in before sowing, and neem cake (about 0.5–1 tonne per hectare, which also slows some soil pests). They improve soil structure and release nutrients slowly. They are good for long-term soil health but are bulky, so use the amount your soil test recommends.",
  "hi": "प्राकृतिक खाद: अच्छी तरह सड़ी गोबर की खाद (बुवाई से पहले लगभग 8–10 टन प्रति हेक्टेयर), कंपोस्ट या वर्मीकंपोस्ट (2–3 टन प्रति हेक्टेयर), बुवाई से पहले जोतकर दबाई गई हरी खाद जैसे ढैंचा या सनई, और नीम खली (लगभग 0.5–1 टन प्रति हेक्टेयर, जो कुछ मिट्टी के कीटों को भी कम करती है)। ये मिट्टी की बनावट सुधारती हैं और पोषक तत्व धीरे छोड़ती हैं। मात्रा मिट्टी जाँच के अनुसार रखें।"},

 {"id": "fert_chemical", "kw_en": ["chemical fertilizer", "urea", "dap", "npk", "potash", "mop", "fertilizer dose", "which fertilizer", "fertilizer for", "harm"],
  "kw_hi": ["रासायनिक खाद", "यूरिया", "डीएपी", "एनपीके", "पोटाश", "खाद की मात्रा", "कौन सी खाद", "नुकसान"],
  "en": "Common chemical fertilizers: urea (46 percent nitrogen), DAP (18 percent nitrogen and 46 percent phosphorus, applied at sowing), muriate of potash (60 percent potassium), and NPK complexes. Apply according to the soil test. Overuse of urea burns roots, pollutes water and lowers soil life, so split nitrogen into two or three doses. Store them dry and keep them away from children and animals.",
  "hi": "सामान्य रासायनिक खाद: यूरिया (46 प्रतिशत नाइट्रोजन), डीएपी (18 प्रतिशत नाइट्रोजन और 46 प्रतिशत फॉस्फोरस, बुवाई के समय), म्यूरिएट ऑफ़ पोटाश (60 प्रतिशत पोटैशियम), और एनपीके मिश्रण। मात्रा मिट्टी जाँच से तय करें। यूरिया ज़्यादा डालने से जड़ें जलती हैं, पानी प्रदूषित होता है और मिट्टी के जीव कम होते हैं, इसलिए नाइट्रोजन दो-तीन बार में दें। सूखी जगह पर रखें और बच्चों व जानवरों से दूर रखें।"},

 {"id": "fert_crop_maize", "kw_en": ["maize", "corn", "fertilizer for maize", "maize fertilizer"], "kw_hi": ["मक्का", "मक्के", "मक्के की खाद"],
  "en": "Maize (general guide): before sowing apply 8–10 tonnes of farmyard manure or 2–3 tonnes of compost per hectare, and a basal dose of DAP and potash as per soil test. Give nitrogen in 2–3 splits: about one-third at sowing, one-third at knee height (about 25–30 days), and the rest at tasselling. Natural options such as compost and neem cake can replace part of the chemical nitrogen. Do not give urea to waterlogged fields.",
  "hi": "मक्का (सामान्य मार्गदर्शन): बुवाई से पहले प्रति हेक्टेयर 8–10 टन गोबर की खाद या 2–3 टन कंपोस्ट डालें, और मिट्टी जाँच के अनुसार डीएपी व पोटाश का आधार खुराक। नाइट्रोजन 2–3 बार में दें: बुवाई पर लगभग एक-तिहाई, घुटने की ऊँचाई पर (लगभग 25–30 दिन) एक-तिहाई, और बाकी झंडे (टैसलिंग) के समय। कंपोस्ट और नीम खली रासायनिक नाइट्रोजन का कुछ हिस्सा बदल सकते हैं। जलभराव वाले खेत में यूरिया न दें।"},

 {"id": "fert_crop_wheat", "kw_en": ["wheat", "fertilizer for wheat"], "kw_hi": ["गेहूँ", "गेहूं", "गेहूँ की खाद"],
  "en": "Wheat (general guide): apply 8–10 tonnes of farmyard manure or compost per hectare before sowing, and DAP and potash at sowing as per soil test. Give nitrogen in 2–3 doses: at sowing, at the first irrigation (crown root stage, about 20–25 days), and sometimes at the second irrigation. Use a natural option such as vermicompost to supply part of the nitrogen.",
  "hi": "गेहूँ (सामान्य मार्गदर्शन): बुवाई से पहले प्रति हेक्टेयर 8–10 टन गोबर की खाद या कंपोस्ट डालें, और मिट्टी जाँच के अनुसार बुवाई के समय डीएपी व पोटाश। नाइट्रोजन 2–3 बार में दें: बुवाई पर, पहली सिंचाई पर (ताज की जड़ अवस्था, लगभग 20–25 दिन), और कभी-कभी दूसरी सिंचाई पर। नाइट्रोजन का कुछ हिस्सा वर्मीकंपोस्ट से दें।"},

 {"id": "fert_crop_rice", "kw_en": ["rice", "paddy", "fertilizer for rice"], "kw_hi": ["धान", "चावल", "चावल की खाद"],
  "en": "Rice (general guide): apply 8–10 tonnes of farmyard manure or compost per hectare before transplanting, and DAP and potash as per soil test at transplanting. Give nitrogen in 2–3 doses: at transplanting or tillering, at the active tillering stage, and at panicle initiation. Green manure such as dhaincha before transplanting also helps. Keep a thin layer of water in the field, but avoid running urea into standing water.",
  "hi": "धान (सामान्य मार्गदर्शन): रोपाई से पहले प्रति हेक्टेयर 8–10 टन गोबर की खाद या कंपोस्ट डालें, और रोपाई के समय मिट्टी जाँच के अनुसार डीएपी व पोटाश। नाइट्रोजन 2–3 बार में दें: रोपाई या कल्ले फूटने पर, सक्रिय कल्ले बनने की अवस्था पर, और बाली बनते समय। रोपाई से पहले ढैंचा जैसी हरी खाद भी मदद करती है।"},

 {"id": "fert_crop_tomato_potato", "kw_en": ["tomato", "potato", "vegetable fertilizer", "fertilizer for tomato", "fertilizer for potato"], "kw_hi": ["टमाटर", "आलू", "सब्ज़ी की खाद"],
  "en": "Tomato and potato (general guide): both need good organic matter. Apply 15–20 tonnes of farmyard manure or 3–4 tonnes of compost per hectare before planting, plus basal DAP and potash as per soil test. Give nitrogen in 2–3 splits, avoiding excess, since too much nitrogen gives leaves but fewer tubers or fruit. Calcium and potassium support fruit and tuber quality.",
  "hi": "टमाटर और आलू (सामान्य मार्गदर्शन): दोनों को अच्छी जैविक खाद चाहिए। रोपाई से पहले प्रति हेक्टेयर 15–20 टन गोबर की खाद या 3–4 टन कंपोस्ट डालें, और मिट्टी जाँच के अनुसार आधार खुराक में डीएपी व पोटाश। नाइट्रोजन 2–3 बार में दें और ज़्यादा न डालें, क्योंकि ज़्यादा नाइट्रोजन से पत्तियाँ बढ़ती हैं पर फल या कंद कम बनते हैं।"},

 {"id": "fert_harm", "kw_en": ["harm", "damage", "too much fertilizer", "overuse", "burn", "bad for crop", "good or bad"],
  "kw_hi": ["नुकसान", "ज़्यादा खाद", "जलना", "बुरा", "अच्छा या बुरा"],
  "en": "Signs of too much fertilizer: dark, very lush leaves with weak stems, leaf tips that burn, and poor fruit or grain set. Too much nitrogen also invites pests and diseases. Too little shows as pale or yellow older leaves and slow growth. Always check with a soil test before adding more. Natural manure is hard to overdose, but chemical nitrogen can damage roots if applied in one large dose.",
  "hi": "ज़्यादा खाद के लक्षण: गहरी, बहुत हरी पत्तियाँ और कमज़ोर तना, पत्ती के सिरे जलना, और फल या दाने कम बनना। ज़्यादा नाइट्रोजन कीट और रोग भी बुलाता है। कम खाद के लक्षण: पुरानी पत्तियों का पीला या फीका होना और धीमी बढ़वार। और खाद डालने से पहले मिट्टी जाँच ज़रूर कराएँ।"},

 {"id": "pest_general", "kw_en": ["pest", "insect", "worm", "bug", "aphid", "whitefly", "spray", "pesticide", "neem spray"],
  "kw_hi": ["कीट", "कीड़ा", "कीड़े", "माहू", "सफ़ेद मक्खी", "स्प्रे", "कीटनाशक", "नीम स्प्रे"],
  "en": "Integrated pest management: scout the field every 2–3 days, check the underside of leaves, and act only when pest levels cross the economic threshold. First use natural methods: yellow sticky traps for whiteflies and aphids, pheromone traps, handpicking, and neem oil spray (about 3–5 ml per litre). If chemicals are needed, use a product registered for that crop and pest, follow the label dose, and rotate modes of action. Keep the spray away from water sources and wear protective gear.",
  "hi": "एकीकृत कीट प्रबंधन: हर 2–3 दिन में खेत की जाँच करें, पत्तियों के नीचे भी देखें, और कीट का स्तर तय सीमा पार करने पर ही कार्रवाई करें। पहले प्राकृतिक तरीके अपनाएँ: सफ़ेद मक्खी और माहू के लिए पीले चिपचिपे ट्रैप, फेरोमोन ट्रैप, हाथ से चुनना, और नीम तेल का छिड़काव (लगभग 3–5 मिली प्रति लीटर)। ज़रूरत हो तो उस फसल और कीट के लिए पंजीकृत दवा लेबल की मात्रा में लें। पानी के स्रोतों से दूर छिड़कें और सुरक्षा उपकरण पहनें।"},

 {"id": "irrigation", "kw_en": ["irrigation", "water", "watering", "irrigate", "how much water", "drip", "sprinkler"],
  "kw_hi": ["सिंचाई", "पानी", "पानी कब दूँ", "ड्रिप", "स्प्रिंकलर", "कितना पानी"],
  "en": "Irrigate by soil moisture, not a fixed calendar. Push a finger 5 cm into the soil: if it feels dry, water. Water early in the morning to reduce evaporation. Drip irrigation saves water and keeps leaves dry, which lowers disease. Avoid waterlogging, which damages roots and invites root rot, especially for pulses and fruit trees.",
  "hi": "सिंचाई मिट्टी की नमी देखकर करें, कैलेंडर से नहीं। 5 सेमी गहराई तक उँगली डालें: सूखी लगे तो पानी दें। सुबह जल्दी सिंचाई करने से भाप कम बनती है। ड्रिप सिंचाई पानी बचाती है और पत्तियाँ सूखी रखती है, जिससे रोग कम होता है। जलभराव से बचें, क्योंकि इससे जड़ें सड़ती हैं, खासकर दालों और फल वृक्षों में।"},

 {"id": "soil_health", "kw_en": ["soil", "soil test", "soil health", "ph of soil", "acidic", "alkaline", "organic carbon"],
  "kw_hi": ["मिट्टी", "मिट्टी जाँच", "मिट्टी की सेहत", "अम्लीय", "क्षारीय"],
  "en": "A soil test (available from your block or soil health card scheme) tells you pH, nitrogen, phosphorus, potassium and organic carbon. Test every 2–3 years. Most crops prefer pH 6 to 7.5. Acidic soil can be improved with lime, alkaline soil with gypsum or organic matter. Add organic matter each season, keep the soil covered, and rotate crops to protect soil life.",
  "hi": "मिट्टी जाँच (ब्लॉक या मृदा स्वास्थ्य कार्ड योजना से) pH, नाइट्रोजन, फॉस्फोरस, पोटैशियम और जैविक कार्बन बताती है। हर 2–3 साल में जाँच करें। ज़्यादातर फसलें pH 6 से 7.5 पसंद करती हैं। अम्लीय मिट्टी में चूना और क्षारीय मिट्टी में जिप्सम या जैविक खाद मदद करती है। हर सीज़न जैविक खाद डालें और फसल चक्र अपनाएँ।"},

 {"id": "fields", "kw_en": ["field", "fields", "add field", "field management", "acres", "soil type", "crop type"],
  "kw_hi": ["खेत", "खेत जोड़ें", "खेत प्रबंधन", "एकड़", "मिट्टी का प्रकार", "फसल का प्रकार"],
  "en": "On Field Management, enter the field name, crop type, cultivated area in acres and soil type, then press Add field. The app refuses blank names, zero area and duplicate names. 'View fields' lists the fields you added in this session. Fields are kept only while the app is open, so write down important details or export them yourself.",
  "hi": "खेत प्रबंधन में खेत का नाम, फसल का प्रकार, एकड़ में क्षेत्रफल और मिट्टी का प्रकार भरकर 'खेत जोड़ें' दबाएँ। खाली नाम, शून्य क्षेत्रफल और दोहराया नाम स्वीकार नहीं होते। 'खेत देखें' में इस सत्र में जोड़े गए खेत दिखते हैं। खेत केवल ऐप खुला रहने तक सहेजे रहते हैं, इसलिए ज़रूरी जानकारी लिख लें।"},

 {"id": "market_prices", "kw_en": ["price", "market", "mandi", "rate", "sell", "selling price", "market price", "agmarknet", "buyer"],
  "kw_hi": ["भाव", "बाज़ार", "मंडी", "रेट", "बेचूँ", "बेचना", "बाज़ार भाव", "खरीदार"],
  "en": "Analytics shows live mandi prices for the commodity you choose, from the government daily price data (data.gov.in). Prices are per quintal (100 kg), with minimum, maximum and modal price for each market. The highest-priced markets are listed first. Prices change daily, so check the arrival date shown. Before selling, compare at least two or three mandis, count transport and commission, and ask about payment timing.",
  "hi": "विश्लेषण में चुनी गई फसल के लाइव मंडी भाव दिखते हैं, जो सरकारी दैनिक भाव डेटा (data.gov.in) से आते हैं। भाव प्रति क्विंटल (100 किलो) हैं, हर मंडी के लिए न्यूनतम, अधिकतम और मॉडल भाव के साथ। सबसे ज़्यादा भाव वाली मंडी पहले दिखती है। भाव रोज़ बदलते हैं, इसलिए आगमन की तारीख देखें। बेचने से पहले कम से कम दो-तीन मंडियों की तुलना करें, किराया और कमीशन जोड़ें, और भुगतान का समय पूछें।"},

 {"id": "selling_where", "kw_en": ["where to sell", "sell my crop", "buyer", "fpo", "apmc", "processor", "export", "startup"],
  "kw_hi": ["कहाँ बेचूँ", "फसल कहाँ बेचूँ", "किसान उत्पादक संगठन", "एफपीओ", "एपीएमसी", "प्रोसेसर", "निर्यात"],
  "en": "Options to sell: the nearest APMC mandi (open market, government-regulated), a Farmer Producer Organisation (FPO) that gives better bargaining, direct sale to food processors or millers, e-NAM (national online market, if your state has joined), and local retailers for fresh produce. Compare prices from the Analytics page, and check the buyer's registration and payment record before you sell.",
  "hi": "बेचने के विकल्प: नज़दीकी एपीएमसी मंडी (सरकारी नियंत्रित खुला बाज़ार), किसान उत्पादक संगठन (एफपीओ) जो बेहतर मोलभाव देता है, खाद्य प्रसंस्करण या मिल वालों को सीधे बिक्री, ई-नाम (राष्ट्रीय ऑनलाइन बाज़ार, अगर आपका राज्य जुड़ा है), और ताज़ा उपज के लिए स्थानीय खुदरा विक्रेता। विश्लेषण पेज से भाव की तुलना करें और बेचने से पहले खरीदार का पंजीकरण व भुगतान रिकॉर्ड जाँचें।"},

 {"id": "startup_ideas", "kw_en": ["startup", "business", "idea", "income", "profit", "value added", "start business", "earn"],
  "kw_hi": ["स्टार्टअप", "व्यवसाय", "आइडिया", "आमदनी", "कमाई", "मुनाफ़ा", "वैल्यू एडेड", "कारोबार"],
  "en": "Farm business ideas linked to common crops: processing (dried chilli, turmeric powder, maize flour, millet snacks), vermicompost or organic fertilizer making, seed and seedling nurseries, fresh produce packing, and farm tourism or direct-to-home vegetable boxes. Start small, check local demand, get a basic business plan checked by your KVK or a bank's agri-business officer, and look for government schemes for food processing and FPOs.",
  "hi": "सामान्य फसलों से जुड़े खेत व्यवसाय: प्रसंस्करण (सूखी मिर्च, हल्दी पाउडर, मक्के का आटा, बाजरे के स्नैक्स), वर्मीकंपोस्ट या जैविक खाद बनाना, बीज और पौध नर्सरी, ताज़ा उपज की पैकिंग, और घर तक सब्ज़ी के डिब्बे। छोटे से शुरू करें, स्थानीय माँग जाँचें, बिज़नेस प्लान KVK या बैंक के कृषि अधिकारी से जँचवाएँ, और खाद्य प्रसंस्करण व FPO की सरकारी योजनाएँ देखें।"},

 {"id": "crop_health_benefit", "kw_en": ["health", "benefit", "nutrition", "good for health", "nutritional value", "why grow"],
  "kw_hi": ["सेहत", "स्वास्थ्य", "फ़ायदा", "पोषण", "सेहत के लिए", "क्यों उगाएँ"],
  "en": "Health benefits of common crops: pulses such as chickpea, moong and lentil give protein and fibre. Maize and millets give energy and fibre. Wheat and rice give carbohydrates; brown rice and whole wheat keep more fibre. Tomato, banana and papaya give vitamins and potassium. Nutrition varies by variety and growing conditions, so use general guidance and not medical advice.",
  "hi": "सामान्य फसलों के स्वास्थ्य लाभ: चना, मूंग और मसूर जैसी दालें प्रोटीन और फाइबर देती हैं। मक्का और बाजरा ऊर्जा और फाइबर देते हैं। गेहूँ और चावल कार्बोहाइड्रेट देते हैं; ब्राउन राइस और साबुत गेहूँ में ज़्यादा फाइबर रहता है। टमाटर, केला और पपीता विटामिन और पोटैशियम देते हैं। पोषण किस्म और उगाने के तरीके पर निर्भर है, यह सामान्य जानकारी है, चिकित्सा सलाह नहीं।"},

 {"id": "settings_language", "kw_en": ["language", "hindi", "english", "switch", "setting", "theme", "dark mode", "light mode", "display"],
  "kw_hi": ["भाषा", "हिंदी", "अंग्रेज़ी", "स्विच", "सेटिंग", "थीम", "डार्क", "लाइट"],
  "en": "Change the language with the English / हिन्दी switch at the top of the left menu. The app follows your browser's light or dark setting, so text stays readable. To change the theme, use the browser or the Streamlit settings menu (three dots at the top right, then Settings).",
  "hi": "बाईं ओर के मेन्यू के ऊपर English / हिन्दी स्विच से भाषा बदलें। ऐप आपके ब्राउज़र की लाइट या डार्क सेटिंग के अनुसार चलता है, ताकि लिखावट पढ़ी जा सके। थीम बदलने के लिए ब्राउज़र या Streamlit सेटिंग का इस्तेमाल करें (ऊपर दाईं ओर तीन बिंदु, फिर Settings)।"},

 {"id": "data_privacy", "kw_en": ["privacy", "data", "safe", "store", "my data", "personal", "secure"],
  "kw_hi": ["गोपनीयता", "डेटा", "सुरक्षित", "निजी", "जानकारी सुरक्षित"],
  "en": "SASYAM does not ask for names, phone numbers or land records. Field records and readings stay in the current session and are not saved to a server by this prototype. Your weather key and market key are kept in your .env file or the hosting provider's secrets, and should never be shared.",
  "hi": "सस्यम नाम, फ़ोन नंबर या ज़मीन के रिकॉर्ड नहीं माँगता। खेत के रिकॉर्ड और रीडिंग इस सत्र में रहते हैं और इस प्रोटोटाइप में सर्वर पर सहेजे नहीं जाते। आपकी मौसम और बाज़ार की चाबी .env फ़ाइल या होस्टिंग के सीक्रेट्स में रहती है, और कभी साझा न करें।"},

 {"id": "model_accuracy", "kw_en": ["accuracy", "how accurate", "trust", "reliable", "correct", "model"],
  "kw_hi": ["सटीकता", "कितना सही", "भरोसा", "भरोसेमंद", "सही है", "मॉडल"],
  "en": "The crop model scores about 96 percent on held-out records of the public crop dataset, and the disease model about 98 percent on held-out PlantVillage photos. These are measured on test data. On a real farm the results can be lower because of different soils, weather and photo quality, so use them as support for your own judgement and local advice.",
  "hi": "फसल मॉडल सार्वजनिक फसल डेटासेट के अलग रखे गए रिकॉर्ड पर लगभग 96 प्रतिशत और रोग मॉडल PlantVillage की अलग रखी फोटो पर लगभग 98 प्रतिशत सटीक है। ये परीक्षण डेटा पर मापे गए हैं। असली खेत में मिट्टी, मौसम और फोटो की गुणवत्ता अलग होने से नतीजे कम हो सकते हैं, इसलिए इन्हें अपने अनुभव और स्थानीय सलाह के साथ इस्तेमाल करें।"},
]
