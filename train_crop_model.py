"""Train the crop recommendation model on the real Kaggle dataset.

Input : data/raw/Crop_recommendation.csv   (columns: N, P, K, temperature, humidity, ph, rainfall, label)
Output: models/crop_model.joblib           (trained decision tree + feature ranges)
        models/crop_model_report.json      (dataset facts and evaluation numbers, for your report)

Run:  python train_crop_model.py [path/to/csv]
"""
import json
import os
import sys
from datetime import date

import joblib
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
TARGET = "label"
MODEL_PATH = os.path.join("models", "crop_model.joblib")
REPORT_PATH = os.path.join("models", "crop_model_report.json")
DEFAULT_CSV = os.path.join("data", "raw", "Crop_recommendation.csv")


def train(csv_path=DEFAULT_CSV, model_path=MODEL_PATH, report_path=REPORT_PATH, seed=42):
    df = pd.read_csv(csv_path)
    missing = [c for c in FEATURES + [TARGET] if c not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing columns: {missing}")
    if df[FEATURES + [TARGET]].isnull().any().any():
        raise ValueError("Dataset contains missing values; clean it before training.")
    X, y = df[FEATURES], df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=seed, stratify=y)
    model = DecisionTreeClassifier(max_depth=10, random_state=seed)
    model.fit(X_train, y_train)
    test_acc = float(model.score(X_test, y_test))
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    cv_scores = cross_val_score(DecisionTreeClassifier(max_depth=10, random_state=seed), X, y, cv=cv)

    # final model on all rows for the app
    final = DecisionTreeClassifier(max_depth=10, random_state=seed).fit(X, y)
    bundle = {
        "model": final,
        "features": FEATURES,
        "classes": sorted(y.unique().tolist()),
        "ranges": {f: [float(df[f].min()), float(df[f].max())] for f in FEATURES},
        "source": "Kaggle: atharvaingle/crop-recommendation-dataset",
    }
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(bundle, model_path)

    report = {
        "dataset": "Crop Recommendation Dataset (Kaggle, atharvaingle)",
        "source_csv": os.path.basename(csv_path),
        "rows": int(len(df)),
        "features": FEATURES,
        "classes": len(bundle["classes"]),
        "rows_per_class_min_max": [int(y.value_counts().min()), int(y.value_counts().max())],
        "model": "DecisionTreeClassifier(max_depth=10)",
        "holdout_test_accuracy": round(test_acc, 4),
        "cv5_accuracy_mean": round(float(cv_scores.mean()), 4),
        "cv5_accuracy_std": round(float(cv_scores.std()), 4),
        "trained_on": date.today().isoformat(),
    }
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    return report


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CSV
    if not os.path.exists(path):
        print(f"Dataset not found at {path}. Run fetch_datasets.py first.")
        sys.exit(1)
    print(json.dumps(train(path), indent=2))
