"""Evaluate a trained fraud detection model."""

from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score

from src.ml.features import FEATURE_COLUMNS, build_features
from src.ml.train import MODEL_PATH


def evaluate(data_path: str, model_path: Path = MODEL_PATH) -> dict:
    df = pd.read_csv(data_path)
    x = build_features(df)
    y = df["is_fraud"]
    model = joblib.load(model_path)
    proba = model.predict_proba(x[FEATURE_COLUMNS])[:, 1]
    preds = (proba >= 0.5).astype(int)
    report = classification_report(y, preds, output_dict=True)
    report["roc_auc"] = roc_auc_score(y, proba)
    return report


if __name__ == "__main__":
    print(evaluate("data/processed/transactions.csv"))
