"""Score a single transaction or a batch of transactions."""

from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd

from src.ml.features import FEATURE_COLUMNS, build_features
from src.ml.train import MODEL_PATH

_model = None


def load_model(model_path: Path = MODEL_PATH):
    global _model
    if _model is None:
        _model = joblib.load(model_path)
    return _model


def predict_proba(records: list[dict], model_path: Path = MODEL_PATH) -> list[float]:
    df = build_features(pd.DataFrame(records))
    model = load_model(model_path)
    return model.predict_proba(df[FEATURE_COLUMNS])[:, 1].tolist()
