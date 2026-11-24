"""Prepare the PlantVillage leaf-image dataset for training.

Input : a copy of the PlantVillage color images, folder layout  <root>/<class_name>/*.jpg
        Get it with:  git clone --depth 1 https://github.com/spMohanty/PlantVillage-Dataset
        (use the raw/color folder inside the clone)
Output: data/processed/plantvillage_64.npz  (images resized to 64x64, labels, class names)

Run:  python prepare_plantvillage.py path/to/PlantVillage-Dataset/raw/color
"""
import json
import os
import sys

import numpy as np
from PIL import Image

SIZE = 64
OUT = os.path.join("data", "processed", "plantvillage_64.npz")


def main(root):
    classes = sorted(d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)))
    X, y = [], []
    for idx, cls in enumerate(classes):
        folder = os.path.join(root, cls)
        for fname in sorted(os.listdir(folder)):
            if not fname.lower().endswith((".jpg", ".jpeg", ".png")):
                continue
            with Image.open(os.path.join(folder, fname)) as im:
                im = im.convert("RGB").resize((SIZE, SIZE), Image.BILINEAR)
                X.append(np.asarray(im, dtype=np.uint8))
                y.append(idx)
        print(f"{idx + 1:2d}/{len(classes)} {cls}: {len(y)} images so far", flush=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    np.savez_compressed(OUT, X=np.stack(X), y=np.array(y, dtype=np.int32), classes=np.array(classes))
    with open(os.path.join("data", "processed", "plantvillage_classes.json"), "w", encoding="utf-8") as f:
        json.dump(classes, f, indent=1, ensure_ascii=False)
    print("saved", OUT, "images:", len(y), "classes:", len(classes))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1])
