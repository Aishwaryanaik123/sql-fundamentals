# Week 9 Day 3 – A/B Test Tracking with MLflow

## Learning Objective
A/B Test Tracking with MLflow – Data Analyst Intern 3M.

## Project Overview
This project compares two variants (A and B) of a landing page to measure conversion performance.

## Dataset
- Total users: 2,000
- Variant A: 1,000 users
- Variant B: 1,000 users
- Conversion and revenue information.

## Tasks Completed
1. Created an A/B testing dataset.
2. Calculated conversion rates.
3. Calculated absolute and relative lift.
4. Performed a two-proportion z-test.
5. Prepared MLflow experiment tracking.
6. Documented experiment results.

## Results

| Metric | Variant A | Variant B |
|---|---:|---:|
| Users | 1000 | 1000 |
| Conversions | 120 | 150 |
| Conversion Rate | 12% | 15% |
| Average Revenue/User | $6.46 | $9.49 |

- Relative lift: 25%
- P-value: 0.049640
- Significance level: 0.05

Conclusion: Variant B shows a statistically significant improvement at the 5% significance level.

## MLflow Tracking
- Experiment: week-9-day-3-ab-test-tracking
- Run: landing-page-variant-comparison
- Parameters, metrics and artifacts are configured in mlflow_tracking.py.

Note: A live MLflow run has not been executed.

## Project Files
- ab_test_data.csv
- ab_test_analysis.py
- mlflow_tracking.py
- analysis_results.csv
- experiment_summary.txt
- process_documentation.txt
- execution_output.txt
- README.md

## Technologies
- Python
- Statistical Hypothesis Testing
- MLflow
- CSV

## Execution
Run the analysis:
python ab_test_analysis.py

Run MLflow tracking in an environment with MLflow installed:
python mlflow_tracking.py

## Note
The dataset is synthetic and created for internship learning purposes.
