-- Recent flagged transactions
SELECT id, amount, timestamp, fraud_score, is_fraud
FROM transactions
WHERE is_fraud = TRUE
ORDER BY timestamp DESC
LIMIT 100;

-- Fraud rate over the last 24 hours
SELECT
    COUNT(*) FILTER (WHERE is_fraud) * 1.0 / NULLIF(COUNT(*), 0) AS fraud_rate,
    COUNT(*) AS total_transactions
FROM transactions
WHERE timestamp >= NOW() - INTERVAL '24 hours';
