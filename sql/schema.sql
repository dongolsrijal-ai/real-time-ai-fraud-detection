CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    amount NUMERIC(12, 2) NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    merchant_risk DOUBLE PRECISION NOT NULL,
    tx_count_1h INTEGER NOT NULL,
    fraud_score DOUBLE PRECISION,
    is_fraud BOOLEAN,
    status VARCHAR(32) NOT NULL DEFAULT 'pending',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_transactions_timestamp ON transactions (timestamp);
CREATE INDEX IF NOT EXISTS idx_transactions_is_fraud ON transactions (is_fraud);
