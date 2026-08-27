"""Publish transactions to Kafka."""

from __future__ import annotations

import json
import os

from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv()


def get_producer() -> KafkaProducer:
    return KafkaProducer(
        bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )


def publish_transaction(transaction: dict) -> None:
    topic = os.getenv("KAFKA_TRANSACTIONS_TOPIC", "transactions")
    producer = get_producer()
    producer.send(topic, transaction)
    producer.flush()


if __name__ == "__main__":
    publish_transaction(
        {
            "amount": 120.50,
            "timestamp": "2026-08-27T12:00:00",
            "merchant_risk": 0.2,
            "tx_count_1h": 1,
        }
    )
