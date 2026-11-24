# SASYAM – Smart Agriculture Advisory System (prototype)

English and Hindi. Seven modules: Dashboard, Weather, Crop Advisor, Disease Detection,
Farm Assistant (chatbot), Field Management, Analytics.

## 1. Set up on your laptop (Windows, macOS or Linux)

You need Python 3.10 or newer.

```bash
# go into the project folder
cd sasyam_prototype

# create and activate a virtual environment
python -m venv .venv
# Windows (PowerShell):   .venv\Scripts\Activate.ps1
# Windows (Command Prompt): .venv\Scripts\activate.bat
# macOS / Linux:          source .venv/bin/activate

pip install -r requirements.txt
```

## 2. Get the real crop dataset (Kaggle)

The app shows a message on the Crop Advisor screen until the model is trained.

1. Create a free account at kaggle.com.
2. Go to Settings > API > "Create New Token". This downloads `kaggle.json`.
3. Put that file in your user folder:
   - Windows: `C:\Users\<you>\.kaggle\kaggle.json`
   - macOS / Linux: `~/.kaggle/kaggle.json`
4. Run:

```bash
python fetch_datasets.py        # downloads data/raw/Crop_recommendation.csv
python train_crop_model.py      # trains the model and writes models/crop_model_report.json
```

If the automatic download does not work, download the dataset by hand from
https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset,
unzip it, and place the CSV at `data/raw/Crop_recommendation.csv`. Then run
`python train_crop_model.py` again.

## 3. Optional: OpenWeatherMap key (for live weather)

1. Create a free key at openweathermap.org.
2. Copy `.env.example` to `.env` and paste your key:
   `OPENWEATHER_API_KEY=your_key_here`

Without a key, the Weather screen shows a clear message and the rest of the app still works.

## 4. Run the app

```bash
streamlit run app.py
```

Your browser opens at http://localhost:8501. Use the language switch at the top of the menu to
change between English and हिन्दी.

## 5. Run the tests (optional)

```bash
python test_logic.py
```

The tests use generated data, so they run without the Kaggle file.

## What is real and what is simulated

| Part | Source |
|---|---|
| Crop Advisor | Real: Kaggle Crop Recommendation Dataset, decision tree trained by `train_crop_model.py` |
| Weather | Live OpenWeatherMap data, needs your key |
| Dashboard and Analytics | Simulated sensor readings (no physical sensors in this prototype) |
| Disease Detection | Upload checks only. No trained disease model is included yet |
| Farm Assistant | Written answers in English and Hindi, three topics |
| Field Management | Entered by the user, kept for the current session |

## Files

- `app.py` – the Streamlit interface
- `logic.py` – rules and models (crop prediction, weather, checks, assistant, analytics)
- `i18n.py` – English and Hindi text
- `fetch_datasets.py` – downloads the Kaggle dataset
- `train_crop_model.py` – trains and saves the crop model and its report
- `test_logic.py` – automated tests
- `DATASETS.md` – dataset sources and how to answer questions about them
- `requirements.txt`, `.env.example`

## Troubleshooting

- **"streamlit is not recognized"**: activate the virtual environment first (step 1).
- **Crop Advisor shows "not trained yet"**: run steps 2 and 4 of the dataset section, then refresh the page.
- **Weather shows "rejected key"**: check the key in `.env` and restart the app.
