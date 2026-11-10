"""Reproducible customer segmentation deep-dive.

Run from project root:
    python -m pip install -r requirements.txt
    python src/run_analysis.py

The pipeline uses customer behavior variables for clustering. Churn is excluded
from model features and used only for post-segmentation profiling.
"""
from pathlib import Path
import logging
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "reports"
LOGS = ROOT / "logs"
FEATURES = ["Total_Orders", "Total_Revenue", "Avg_Order_Value",
            "Tenure_Days", "Recency_Days"]
SEGMENT_NAMES = {
    1: "Low-frequency, high-ticket / churn-risk",
    2: "High-frequency, short-tenure anomaly",
    3: "High-value, recently active",
    4: "Frequent, low-spend",
    5: "Established, mid-value / less recent",
}

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(filename=LOGS / "analysis.log", level=logging.INFO,
                        format="%(asctime)s | %(levelname)s | %(message)s")
    df = pd.read_csv(RAW / "da_customer_profiles.csv")
    for col in ["First_Purchase_Date", "Last_Purchase_Date"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    snapshot_date = df["Last_Purchase_Date"].max()
    df["Tenure_Days"] = (df["Last_Purchase_Date"] -
                         df["First_Purchase_Date"]).dt.days.clip(lower=0)
    df["Recency_Days"] = (snapshot_date -
                          df["Last_Purchase_Date"]).dt.days.clip(lower=0)
    df["Avg_Order_Value"] = df["Total_Revenue"] / df["Total_Orders"].replace(0, pd.NA)

    x = df[FEATURES].copy()
    x = x.fillna(x.median(numeric_only=True))
    x_log = __import__("numpy").log1p(x)
    scaled = StandardScaler().fit_transform(x_log)

    selection = []
    for k in range(2, 6):
        candidate = KMeans(n_clusters=k, random_state=42, n_init=20)
        labels = candidate.fit_predict(scaled)
        selection.append({
            "k": k,
            "silhouette_score": round(float(silhouette_score(scaled, labels)), 4),
            "min_cluster_size": int(pd.Series(labels).value_counts().min())
        })
    pd.DataFrame(selection).to_csv(OUT / "model_selection_silhouette.csv", index=False)
    best_k = max(selection, key=lambda item: item["silhouette_score"])["k"]

    model = KMeans(n_clusters=best_k, random_state=42, n_init=20)
    df["Cluster"] = model.fit_predict(scaled) + 1
    df["Segment"] = df["Cluster"].map(SEGMENT_NAMES)

    profile = df.groupby("Cluster").agg(
        Customers=("Customer_ID", "count"),
        Avg_Orders=("Total_Orders", "mean"),
        Avg_Revenue=("Total_Revenue", "mean"),
        Median_Revenue=("Total_Revenue", "median"),
        Avg_Order_Value=("Avg_Order_Value", "mean"),
        Avg_Tenure_Days=("Tenure_Days", "mean"),
        Avg_Recency_Days=("Recency_Days", "mean"),
        Churned_Customers=("Churned", "sum"),
        Churn_Rate_Pct=("Churned", lambda s: 100 * s.mean())
    ).round(2)
    profile.insert(0, "Segment", [SEGMENT_NAMES[i] for i in profile.index])
    profile.to_csv(OUT / "segment_profiles.csv")

    export = df.copy()
    for col in ["First_Purchase_Date", "Last_Purchase_Date"]:
        export[col] = export[col].dt.strftime("%Y-%m-%d")
    export.to_csv(OUT / "customer_segment_assignments.csv", index=False)

    channel = df.groupby("Acquisition_Channel").agg(
        Customers=("Customer_ID", "count"),
        Avg_Revenue=("Total_Revenue", "mean"),
        Total_Revenue=("Total_Revenue", "sum"),
        Churn_Rate_Pct=("Churned", lambda s: 100 * s.mean())
    ).round(2).sort_values("Total_Revenue", ascending=False)
    channel.to_csv(OUT / "acquisition_channel_profile.csv")

    age = df.groupby("Age_Band").agg(
        Customers=("Customer_ID", "count"),
        Avg_Revenue=("Total_Revenue", "mean"),
        Churn_Rate_Pct=("Churned", lambda s: 100 * s.mean())
    ).round(2)
    age.to_csv(OUT / "age_band_profile.csv")
    logging.info("Completed segmentation: n=%s, k=%s, snapshot=%s",
                 len(df), best_k, snapshot_date.date())
    print(f"Analysis complete: {len(df)} customers, k={best_k}, "
          f"snapshot={snapshot_date.date()}. See reports/.")

if __name__ == "__main__":
    main()
