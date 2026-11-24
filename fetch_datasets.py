"""Download the real datasets used by SASYAM.

Crop recommendation (Kaggle, Atharva Ingle, 2,200 rows, 22 crops):
    https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset

Requires a Kaggle API token: put kaggle.json in ~/.kaggle/ (Kaggle > Settings > API > Create New Token).
Then run:  python fetch_datasets.py
"""
import os
import shutil
import subprocess
import sys

RAW_DIR = os.path.join("data", "raw")
CROP_SLUG = "atharvaingle/crop-recommendation-dataset"


def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    target = os.path.join(RAW_DIR, "Crop_recommendation.csv")
    if os.path.exists(target):
        print(f"Already present: {target}")
        return 0
    kaggle = shutil.which("kaggle")
    if kaggle is None:
        print("The Kaggle command-line tool is not installed. Run:  pip install kaggle")
        return 1
    cmd = [kaggle, "datasets", "download", "-d", CROP_SLUG, "-p", RAW_DIR, "--unzip"]
    print("Running:", " ".join(cmd))
    res = subprocess.run(cmd)
    if res.returncode != 0:
        print("Download failed. Check your kaggle.json token and internet connection.")
        return res.returncode
    if not os.path.exists(target):
        print(f"Expected {target} after download but it was not found. Check the contents of {RAW_DIR}.")
        return 1
    print(f"Saved {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
