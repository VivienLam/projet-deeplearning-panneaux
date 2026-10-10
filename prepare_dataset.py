import os
import glob
import cv2
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

PROJET_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJET_DIR, "data")
TRAIN_DIR = os.path.join(DATA_DIR, "GTSRB", "Final_Training", "Images")
TEST_DIR = os.path.join(DATA_DIR, "GTSRB", "Final_Test", "Images")
TEST_CSV = os.path.join(DATA_DIR, "GT-final_test.csv")
OUTPUT_NPZ = os.path.join(DATA_DIR, "gtsrb_32x32.npz")

IMG_SIZE = (32, 32)

def prepare_data():
    print("=== Chargement et Prétraitement du Train Set ===")
    train_images = []
    train_labels = []

    for class_id in range(43):
        folder = os.path.join(TRAIN_DIR, f"{class_id:05d}")
        if not os.path.exists(folder):
            print(f"Warning: folder {folder} not found")
            continue
        csv_file = os.path.join(folder, f"GT-{class_id:05d}.csv")
        df_class = pd.read_csv(csv_file, sep=";")
        
        for _, row in df_class.iterrows():
            img_path = os.path.join(folder, row["Filename"])
            img = cv2.imread(img_path)
            if img is None:
                continue
            # Conversion BGR -> RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # Redimensionnement uniforme
            img_resized = cv2.resize(img, IMG_SIZE)
            train_images.append(img_resized)
            train_labels.append(row["ClassId"])

    X_train_raw = np.array(train_images, dtype=np.uint8)
    y_train_raw = np.array(train_labels, dtype=np.int64)

    print(f"Images train chargées : {X_train_raw.shape}, labels : {y_train_raw.shape}")

    print("=== Chargement et Prétraitement du Test Set ===")
    test_images = []
    test_labels = []

    df_test = pd.read_csv(TEST_CSV, sep=";")
    for _, row in df_test.iterrows():
        img_path = os.path.join(TEST_DIR, row["Filename"])
        img = cv2.imread(img_path)
        if img is None:
            continue
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_resized = cv2.resize(img, IMG_SIZE)
        test_images.append(img_resized)
        test_labels.append(row["ClassId"])

    X_test = np.array(test_images, dtype=np.uint8)
    y_test = np.array(test_labels, dtype=np.int64)

    print(f"Images test chargées : {X_test.shape}, labels : {y_test.shape}")

    # Split train / validation stratifié (80% / 20%)
    print("=== Découpage Train / Validation Stratifié ===")
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_raw, y_train_raw,
        test_size=0.20,
        random_state=42,
        stratify=y_train_raw
    )

    print(f"Train set : X={X_train.shape}, y={y_train.shape}")
    print(f"Val set   : X={X_val.shape}, y={y_val.shape}")
    print(f"Test set  : X={X_test.shape}, y={y_test.shape}")

    print(f"Sauvegarde dans {OUTPUT_NPZ}...")
    np.savez_compressed(
        OUTPUT_NPZ,
        X_train=X_train, y_train=y_train,
        X_val=X_val, y_val=y_val,
        X_test=X_test, y_test=y_test
    )
    print("Sauvegarde terminée avec succès !")

if __name__ == "__main__":
    prepare_data()

