# Methodology and assumptions – customer segmentation

## 1. Deep-dive selection
The primary deep-dive is **behavioral customer segmentation**. The customer profile file is the appropriate source because it contains customer-level purchase frequency, revenue, first/last purchase dates, acquisition channel, age band, and a churn indicator. The property listings and product catalogue are included in `data/raw/` as project context but are not joined to customers: no shared relationship key is supplied.

## 2. Objective
Identify groups of customers with similar purchase behavior to support differentiated engagement, retention, and customer-value strategies.

## 3. Data and unit of analysis
- Source: `data/raw/da_customer_profiles.csv`
- Records: 200 customers
- Grain: one row per customer
- Candidate key: `Customer_ID`
- Snapshot reference date: 2026-07-07, the maximum `Last_Purchase_Date` in the supplied data.

## 4. Feature engineering
The clustering features are:
1. `Total_Orders` – purchase frequency.
2. `Total_Revenue` – cumulative customer revenue.
3. `Avg_Order_Value` – `Total_Revenue / Total_Orders`.
4. `Tenure_Days` – days between first and last recorded purchase.
5. `Recency_Days` – days between a customer's last purchase and the dataset snapshot date.

The features are transformed using `log1p` to reduce right skew and standardized using `StandardScaler`. Missing numeric feature values, if any, are imputed with the feature median. `Churned`, `Gender`, `Age_Band`, `City`, and `Acquisition_Channel` are not used to fit clusters. They are retained for post-cluster interpretation. Excluding churn from model features avoids directly building the churn outcome into the segments.

## 5. Model selection
K-Means was evaluated for k = 2, 3, 4, and 5 using silhouette score. The selected solution is k = 5, with a silhouette score of 0.3223. The result is reproducible with `random_state=42` and `n_init=20`. Silhouette scores around this range indicate moderate/overlapping separation; segments should be treated as useful exploratory groupings, not naturally discrete customer types.

## 6. Segment interpretation
- **Low-frequency, high-ticket / churn-risk (Segment 1):** 36 customers; average revenue 25,513.14; average orders 3.11; churn rate 16.67%.
- **High-frequency, short-tenure anomaly (Segment 2):** 39 customers; average revenue 25,127.74; average orders 14.28; churn rate 0.00%.
- **High-value, recently active (Segment 3):** 34 customers; average revenue 32,762.32; average orders 10.06; churn rate 0.00%.
- **Frequent, low-spend (Segment 4):** 24 customers; average revenue 4,136.12; average orders 14.21; churn rate 0.00%.
- **Established, mid-value / less recent (Segment 5):** 67 customers; average revenue 28,074.33; average orders 14.25; churn rate 0.00%.

## 7. Key assumptions and limitations
- Each row represents one customer and `Customer_ID` is unique.
- `Total_Revenue` is cumulative for the observation period; currency/unit is not specified and is therefore reported in source units.
- `Total_Orders` is assumed to be a positive count.
- The dataset snapshot is defined as the latest `Last_Purchase_Date` (2026-07-07), not today's date. Recency therefore measures relative recency within the supplied extract, not days since the current date.
- `Tenure_Days` is calculated from first to last purchase date; it is not customer age or account age.
- The data is customer-level aggregate data, not transaction-level history. This prevents a full monthly cohort-retention curve or detailed purchase-sequence analysis.
- Only 6 customers are flagged as churned (3.00%). Churn-rate comparisons are descriptive and should not be treated as statistically conclusive.
- Cluster numbers are algorithmic IDs. Segment names are human-readable interpretations of observed profiles.
- The second segment has a very short average first-to-last purchase span despite high order frequency. This is a data-validation flag: confirm source date semantics before operational targeting.
- No causal claims are made. Segmentation does not prove that acquisition channel, age, or recency causes revenue or churn.

## 8. Recommended business actions
- **Low-frequency, high-ticket / churn-risk:** prioritize personalized re-engagement and validate whether high order values represent a small number of large transactions.
- **High-frequency, short-tenure anomaly:** audit purchase dates and order-count semantics before campaigns; if confirmed, support with onboarding and repeat-purchase journeys.
- **High-value, recently active:** protect the relationship with loyalty benefits, relevant cross-sell, and service-quality monitoring.
- **Frequent, low-spend:** test bundles, threshold-based offers, and basket-building recommendations with margin safeguards.
- **Established, mid-value / less recent:** run a measured win-back campaign and monitor response.

## 9. Reproducibility
Run `python src/run_analysis.py` after installing `requirements.txt`. The script regenerates customer assignments, segment profiles, silhouette comparison, and channel/age profiles in `reports/`. The report PDF summarizes the current supplied-data run.
