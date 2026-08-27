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

## Local setup

This project requires **Python 3.12**.

### Windows (PowerShell)

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -q
python -m uvicorn src.api.main:app --reload
```

### POSIX (macOS / Linux)

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -q
python -m uvicorn src.api.main:app --reload
```

With the API running, open:

- Health check: http://127.0.0.1:8000/health
- Interactive docs: http://127.0.0.1:8000/docs

`GET /health` should return `{"status": "ok"}`.

## Pipeline

1. Train a model with `src/ml/train.py`
2. Serve scores through `src/api/main.py`
3. Stream transactions with `src/streaming/producer.py` and `src/streaming/consumer.py`
4. Persist results via `src/database/`
