# SASYAM – Datasets, models and results

## 1. Crop recommendation (real dataset)
- **Name:** Crop Recommendation Dataset, originally published on Kaggle by Atharva Ingle.
  https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset
- **Copy used here:** `data/raw/Crop_recommendation.csv`, taken from a public GitHub copy
  (github.com/aakashr02/Crop-Recommendation). Check it against the Kaggle file before citing.
- **Size:** 2,200 rows, 22 crops, 100 rows per crop, no missing values.
- **Inputs:** N, P, K, temperature (°C), humidity (%), ph, rainfall (mm). **Target:** crop label.
- **Model:** decision tree, max depth 10, 80/20 stratified split, 5-fold cross-validation.
- **Results (from `models/crop_model_report.json`):** holdout test accuracy **96.36%**;
  5-fold CV accuracy **98.5% ± 0.7%**.

## 2. Leaf disease detection (real dataset, trained model)
- **Name:** PlantVillage, color images (Hughes & Salathé 2015; Mohanty, Hughes & Salathé 2016).
  Repository: https://github.com/spMohanty/PlantVillage-Dataset (folder `raw/color`).
- **Size:** 54,305 images, 38 classes. Used at 64 × 64 pixels (`data/processed/plantvillage_64.npz`).
- **Split:** 80/10/10 stratified, seed 42 → 43,444 train / 5,430 validation / 5,431 test.
- **Model:** compact CNN trained from scratch (no pretrained weights; they could not be downloaded
  in the training environment). 12 epochs, about 41 minutes on one CPU core.
- **Results (from `models/disease_model_report.json`):** test accuracy **98.38%**, macro F1 **0.979**.
  Weakest class: Tomato early blight, F1 0.908.
- **Caveat:** random split. PlantVillage has several photos of the same leaf, so accuracy on new
  leaves and field photos is expected to be lower. Field photos have not been tested.

## 3. Weather (live service, not a dataset)
- OpenWeatherMap current weather API. **Yes, you need your own key**: sign up free at
  openweathermap.org, copy the key, and put it in `.env` locally or in Streamlit Secrets when deployed.
  Keys can take a short time to activate after signup. I cannot create one for you.

## 4. Dashboard and Analytics (simulated)
- Sensor readings are generated in code. No physical sensors or farm data are used.

## 5. Farm assistant and fields
- Assistant answers are written by the team (English and Hindi, three topics).
- Field records are entered by the user and kept for the session only.

## Reproduce everything

```bash
pip install -r requirements-train.txt
python fetch_datasets.py                          # crop CSV via Kaggle (or copy it by hand)
python train_crop_model.py data/raw/Crop_recommendation.csv
git clone --depth 1 https://github.com/spMohanty/PlantVillage-Dataset
python prepare_plantvillage.py PlantVillage-Dataset/raw/color
python train_disease_model.py
streamlit run app.py
```

## Suggested answer for faculty
> "Crop recommendation uses the Kaggle Crop Recommendation Dataset: 2,200 records, seven soil and
> climate features, 22 crops. A decision tree reaches 96.4% on held-out data. Disease detection uses
> PlantVillage, 54,305 leaf images in 38 classes. A convolutional network trained from scratch reaches
> 98.4% on a held-out split, which is optimistic for new leaves, and we state that limit. Weather comes
> from the OpenWeatherMap API. Dashboard readings are simulated and labelled as such."
