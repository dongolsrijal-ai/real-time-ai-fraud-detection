"""SQLAlchemy models for transactions and fraud scores."""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    merchant_risk: Mapped[float] = mapped_column(Float, nullable=False)
    tx_count_1h: Mapped[int] = mapped_column(Integer, nullable=False)
    fraud_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    is_fraud: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    status: Mapped[str] = mapped_column(String(32), default="pending")
