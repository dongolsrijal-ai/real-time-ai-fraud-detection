"""Feature engineering for fraud detection."""

from __future__ import annotations

import pandas as pd


FEATURE_COLUMNS = [
    "amount",
    "hour_of_day",
    "is_weekend",
    "merchant_risk",
    "tx_count_1h",
]


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Return a dataframe with model-ready feature columns."""
    features = df.copy()
    if "timestamp" in features.columns:
        ts = pd.to_datetime(features["timestamp"])
        features["hour_of_day"] = ts.dt.hour
        features["is_weekend"] = (ts.dt.dayofweek >= 5).astype(int)
    return features[FEATURE_COLUMNS]
