"""Train the leaf disease classifier on the PlantVillage images prepared by prepare_plantvillage.py.

Input : data/processed/plantvillage_64.npz
Output: models/disease_model.keras        trained network
        models/disease_classes.json       class names in output order
        models/disease_model_report.json  test accuracy, macro F1 and per-class scores

Split: stratified 80 / 10 / 10 (train / validation / test), fixed seed.
Caveat: PlantVillage contains several photographs of the same leaf, so a random split can
overstate accuracy on new leaves. The report states this limit.

Run:  python train_disease_model.py
"""
import json
import os
import time

import numpy as np
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import train_test_split

SEED = 42
DATA = os.path.join("data", "processed", "plantvillage_64.npz")
MODEL_PATH = os.path.join("models", "disease_model.keras")
CLASSES_PATH = os.path.join("models", "disease_classes.json")
REPORT_PATH = os.path.join("models", "disease_model_report.json")
EPOCHS = int(os.environ.get("SASYAM_EPOCHS", "12"))
BATCH = 64


def build_model(n_classes, size=64):
    import tensorflow as tf
    from tensorflow.keras import layers, models
    inp = layers.Input(shape=(size, size, 3))
    x = layers.Rescaling(1.0 / 255)(inp)
    x = layers.RandomFlip("horizontal")(x)  # augmentation, active only during training
    for filters in (32, 64, 128, 128):
        x = layers.Conv2D(filters, 3, padding="same", use_bias=False)(x)
        x = layers.BatchNormalization()(x)
        x = layers.ReLU()(x)
        x = layers.MaxPooling2D()(x)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(128, activation="relu")(x)
    x = layers.Dropout(0.3)(x)
    out = layers.Dense(n_classes, activation="softmax")(x)
    model = models.Model(inp, out)
    model.compile(optimizer=tf.keras.optimizers.Adam(1e-3),
                  loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model


def main():
    import tensorflow as tf
    data = np.load(DATA)
    X, y, classes = data["X"], data["y"], [str(c) for c in data["classes"]]
    X_tr, X_tmp, y_tr, y_tmp = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEED)
    X_val, X_te, y_val, y_te = train_test_split(X_tmp, y_tmp, test_size=0.5, stratify=y_tmp, random_state=SEED)
    print(f"train {len(y_tr)}  val {len(y_val)}  test {len(y_te)}  classes {len(classes)}", flush=True)

    model = build_model(len(classes))
    cb = [
        tf.keras.callbacks.EarlyStopping(monitor="val_accuracy", patience=3, restore_best_weights=True),
        tf.keras.callbacks.ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=1, verbose=1),
    ]
    t0 = time.time()
    hist = model.fit(X_tr, y_tr, validation_data=(X_val, y_val), epochs=EPOCHS, batch_size=BATCH,
                     callbacks=cb, verbose=2)
    train_minutes = (time.time() - t0) / 60

    probs = model.predict(X_te, batch_size=256, verbose=0)
    pred = probs.argmax(axis=1)
    acc = float((pred == y_te).mean())
    macro_f1 = float(f1_score(y_te, pred, average="macro"))
    per_class = classification_report(y_te, pred, target_names=classes, output_dict=True, zero_division=0)

    os.makedirs("models", exist_ok=True)
    model.save(MODEL_PATH)
    with open(CLASSES_PATH, "w", encoding="utf-8") as f:
        json.dump(classes, f, indent=1, ensure_ascii=False)
    report = {
        "dataset": "PlantVillage color images (spMohanty/PlantVillage-Dataset, raw/color)",
        "images_total": int(len(y)), "classes": len(classes),
        "split": {"train": int(len(y_tr)), "validation": int(len(y_val)), "test": int(len(y_te))},
        "image_size": 64, "epochs_run": len(hist.history["loss"]), "epochs_max": EPOCHS,
        "training_minutes": round(train_minutes, 1),
        "test_accuracy": round(acc, 4), "test_macro_f1": round(macro_f1, 4),
        "worst_classes_f1": sorted(
            [(c, round(per_class[c]["f1-score"], 3)) for c in classes], key=lambda t: t[1])[:5],
        "caveat": "Random split: several photos of the same leaf can appear in train and test, "
                  "so accuracy on new leaves may be lower.",
    }
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(json.dumps(report, indent=2, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
