# Anomaly Detection — Isolation Forest + Statistical Methods
**Data Analyst Intern 3M | Week 10 Day 3**

## Objective
Identify unusual transaction-like records using statistical outlier detection and the unsupervised Isolation Forest algorithm, then compare their results.

## Project structure
- `data/synthetic_transaction_data.csv` — 1,200 synthetic records with five numeric features and a planted evaluation label.
- `src/anomaly_detection.py` — reproducible analysis script.
- `reports/anomaly_detection_report.html` — report with methods, results, charts, and interpretation.
- `reports/anomaly_detection_results.csv` — row-level method flags and anomaly votes.
- `reports/method_comparison.csv` — precision, recall, F1, and flagged counts.
- `reports/*.png` — generated charts.
- `experiment_process.md` — documented workflow and decisions.
- `execution_notes.txt` — execution summary and limitations.

## Methods
1. **Z-score:** flags a record if any feature is at least 3 standard deviations from its mean.
2. **IQR:** flags a record if any feature lies outside the Q1 − 1.5×IQR and Q3 + 1.5×IQR fences.
3. **Isolation Forest:** unsupervised model with 200 trees, contamination 3%, and fixed random seed.
4. **Combined vote:** flags a record when at least two methods agree.

## Reproduce
Python 3.10+ is recommended.
```bash
python -m pip install -r requirements.txt
python src/anomaly_detection.py
```
The script reads the supplied CSV and recreates the scored records, method comparison, and flagged-count chart in `reports/`.

## Demonstration results
The dataset contains 1,200 records, including 36 deliberately injected unusual records. See `reports/method_comparison.csv` and `reports/anomaly_detection_report.html` for the computed results.

## Important limitations
This is a **synthetic educational dataset**, not actual customer, financial, or Indian market data. The unusual records were intentionally made pronounced; therefore, perfect scores for some methods are a property of this controlled demonstration and do not indicate real-world expected performance. The planted label is used only for evaluation and is not included as a model feature. Real deployments require representative data, careful threshold tuning, validation, and human review.
