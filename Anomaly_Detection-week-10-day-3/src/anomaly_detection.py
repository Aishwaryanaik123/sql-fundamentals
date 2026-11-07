"""
Anomaly Detection: Isolation Forest + Statistical Methods
Run from the project root: python src/anomaly_detection.py
Dataset is synthetic and intended for learning/demo purposes.
"""
from pathlib import Path
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_transaction_data.csv"
OUT = ROOT / "reports"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
features = [
    "transaction_amount", "transaction_count_24h", "account_age_days",
    "transaction_hour", "distance_from_usual_km"
]
X = df[features]
y = df["known_injected_anomaly"]

# Statistical method 1: absolute Z-score threshold
z = ((X - X.mean()) / X.std(ddof=0)).abs()
df["zscore_anomaly"] = (z >= 3).any(axis=1).astype(int)

# Statistical method 2: IQR fences
q1, q3 = X.quantile(0.25), X.quantile(0.75)
iqr = q3 - q1
df["iqr_anomaly"] = (
    ((X < (q1 - 1.5 * iqr)) | (X > (q3 + 1.5 * iqr))).any(axis=1)
).astype(int)

# Isolation Forest is unsupervised; injected label is used only for evaluation.
forest = IsolationForest(n_estimators=200, contamination=0.03, random_state=42)
df["isolation_forest_anomaly"] = (forest.fit_predict(X) == -1).astype(int)

votes = df[["zscore_anomaly", "iqr_anomaly", "isolation_forest_anomaly"]].sum(axis=1)
df["anomaly_votes"] = votes
df["combined_anomaly"] = (votes >= 2).astype(int)

def score(name, predictions):
    return {
        "method": name,
        "precision": round(precision_score(y, predictions, zero_division=0), 4),
        "recall": round(recall_score(y, predictions, zero_division=0), 4),
        "f1_score": round(f1_score(y, predictions, zero_division=0), 4),
        "flagged_records": int(predictions.sum()),
    }

comparison = pd.DataFrame([
    score("Z-score", df["zscore_anomaly"]),
    score("IQR", df["iqr_anomaly"]),
    score("Isolation Forest", df["isolation_forest_anomaly"]),
    score("Combined vote (2 of 3)", df["combined_anomaly"]),
])
df.to_csv(OUT / "anomaly_detection_results.csv", index=False)
comparison.to_csv(OUT / "method_comparison.csv", index=False)

plt.figure(figsize=(9, 5))
plt.bar(comparison["method"], comparison["flagged_records"])
plt.title("Anomalies Flagged by Detection Method")
plt.ylabel("Number of records flagged")
plt.xticks(rotation=18, ha="right")
plt.tight_layout()
plt.savefig(OUT / "flagged_counts.png", dpi=160)
plt.close()
print(comparison.to_string(index=False))
print(f"Saved scored records and comparison to: {OUT}")
