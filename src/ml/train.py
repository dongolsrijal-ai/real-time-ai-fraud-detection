"""Train a fraud detection model and save it under models/."""

from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from src.ml.features import FEATURE_COLUMNS, build_features

MODEL_PATH = Path("models/fraud_model.joblib")


def train(data_path: str, model_path: Path = MODEL_PATH) -> Path:
    df = pd.read_csv(data_path)
    x = build_features(df)
    y = df["is_fraud"]
    x_train, _, y_train, _ = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
    model.fit(x_train[FEATURE_COLUMNS], y_train)

    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    return model_path


if __name__ == "__main__":
    train("data/processed/transactions.csv")
