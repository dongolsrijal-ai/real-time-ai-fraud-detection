"""Fraud scoring API."""

from __future__ import annotations

import os
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from src.ml.predict import predict_proba

load_dotenv()

app = FastAPI(title="Real-Time AI Fraud Detection")
THRESHOLD = float(os.getenv("FRAUD_THRESHOLD", "0.5"))


class Transaction(BaseModel):
    amount: float
    timestamp: str
    merchant_risk: float
    tx_count_1h: int
    hour_of_day: Optional[int] = None
    is_weekend: Optional[int] = None


class ScoreResponse(BaseModel):
    fraud_score: float
    is_fraud: bool


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/score", response_model=ScoreResponse)
def score(tx: Transaction) -> ScoreResponse:
    fraud_score = predict_proba([tx.model_dump()])[0]
    return ScoreResponse(fraud_score=fraud_score, is_fraud=fraud_score >= THRESHOLD)
