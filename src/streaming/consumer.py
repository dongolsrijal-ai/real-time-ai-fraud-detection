"""Consume transactions, score them, and publish results."""

from __future__ import annotations

import json
import os

from dotenv import load_dotenv
from kafka import KafkaConsumer, KafkaProducer

from src.ml.predict import predict_proba

load_dotenv()

THRESHOLD = float(os.getenv("FRAUD_THRESHOLD", "0.5"))


def run() -> None:
    consumer = KafkaConsumer(
        os.getenv("KAFKA_TRANSACTIONS_TOPIC", "transactions"),
        bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
        group_id=os.getenv("KAFKA_CONSUMER_GROUP", "fraud-detector"),
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    )
    producer = KafkaProducer(
        bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    scores_topic = os.getenv("KAFKA_SCORES_TOPIC", "fraud-scores")

    for message in consumer:
        tx = message.value
        score = predict_proba([tx])[0]
        producer.send(
            scores_topic,
            {**tx, "fraud_score": score, "is_fraud": score >= THRESHOLD},
        )


if __name__ == "__main__":
    run()
