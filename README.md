# Real-Time AI Fraud Detection

Detect fraudulent transactions in real time using a machine learning model, a streaming pipeline, and a scoring API.

## Project layout

```
real-time-ai-fraud-detection/
├── data/           # raw and processed datasets
├── notebooks/      # exploratory analysis
├── src/            # application code (ML, API, streaming, database)
├── sql/            # schema and queries
├── dashboard/      # monitoring UI
├── docker/         # extra Dockerfiles and image config
├── kubernetes/     # k8s manifests
├── terraform/      # infrastructure as code
├── tests/          # unit and integration tests
└── models/         # trained model artifacts
```

## Quick start

1. Copy environment variables: `cp .env.example .env`
2. Install dependencies: `pip install -r requirements.txt`
3. Run services: `docker compose up`

## Pipeline

1. Train a model with `src/ml/train.py`
2. Serve scores through `src/api/main.py`
3. Stream transactions with `src/streaming/producer.py` and `src/streaming/consumer.py`
4. Persist results via `src/database/`
