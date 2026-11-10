# Week 4 – Customer Segmentation Deep-Dive

## Objective
Conduct the primary analytical deep-dive using behavioral customer segmentation. Identify actionable customer groups from the supplied customer profile data and document methodology, assumptions, limitations, and recommendations.

## Selected analytical approach
**K-Means customer segmentation** was selected instead of churn prediction or cohort retention because the dataset has customer-level aggregate behavior fields but only 6 churned customers (3.0%) and no transaction-level monthly history. Segmentation is therefore more appropriate and avoids overclaiming predictive performance.

## Results at a glance
- Customers analyzed: 200
- Total recorded revenue: 4,992,621 source units
- Average revenue per customer: 24,963.10 source units
- Churn flag rate: 3.00% (6 customers)
- Selected cluster count: 5
- Best silhouette score among k=2–5: 0.3223
- Snapshot reference date for recency: 2026-07-07

## Run locally
Python 3.9+ recommended.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/run_analysis.py
```

## Outputs
- `reports/customer_segment_assignments.csv` – customer-level segment assignment.
- `reports/segment_profiles.csv` – segment sizes, average behavior and churn profile.
- `reports/model_selection_silhouette.csv` – model selection results for k=2–5.
- `reports/acquisition_channel_profile.csv` – supporting acquisition-channel profile.
- `reports/age_band_profile.csv` – supporting age-band profile.
- `reports/data_quality_summary.csv` – source quality check.
- `reports/methodology_and_assumptions.md` – full methodology, assumptions and limitations.
- `Week_4_Customer_Segmentation_Deep_Dive_Report.pdf` – submission-ready report.

## Data scope
All three supplied datasets are retained in `data/raw/`. The customer profile dataset is the modeling source. Real estate listings and product catalogue are not joined because no supported customer-to-listing/product relationship key is provided.

## Version control
The project is designed to be added as a standalone folder on a separate feature branch. Do not commit unrelated project folders or merge into `master`/`main` unless explicitly instructed.

## Important limitations
This is exploratory segmentation, not a predictive churn model. Cluster separation is moderate, the dataset is an aggregate customer snapshot, and the business meaning of currency, churn, and date fields should be confirmed with the stakeholder.
