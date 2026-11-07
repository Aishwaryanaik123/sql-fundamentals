# Week 9 Day 4 – MLflow Dashboard: Compare Model Versions

## Objective
Compare three model versions using common evaluation metrics and present the comparison in a dashboard.

## Important data note
This package uses illustrative demonstration metrics. No model was trained and no live MLflow run was executed. `dashboard.html` is a standalone offline report, not the live MLflow UI.

## Results

| Version | Accuracy | Precision | Recall | F1 score | ROC-AUC | Training time |
|---|---:|---:|---:|---:|---:|---:|
| v1.0 | 0.842 | 0.831 | 0.806 | 0.818 | 0.879 | 18.4 s |
| v1.1 | 0.861 | 0.849 | 0.832 | 0.840 | 0.901 | 20.1 s |
| v1.2 | 0.873 | 0.866 | 0.845 | 0.855 | 0.914 | 22.7 s |

## Findings
- v1.2 leads on all listed predictive metrics.
- Accuracy improves by 3.1 percentage points from v1.0 to v1.2.
- Training time increases by 4.3 seconds.
- v1.2 is the preferred candidate for further validation.

## Files
- `dashboard.html` – standalone comparison dashboard; open in a browser.
- `model_versions.csv` – comparison data.
- `model_comparison.py` – standard-library comparison script.
- `mlflow_tracking.py` – optional MLflow logging example; requires MLflow.
- `experiment_process.md` – workflow and interpretation.
- `experiment_summary.txt` – concise results.
- `execution_output.txt` – sample script output.
- `requirements_optional.txt` – optional dependency note.

## View without installation
Open `dashboard.html` in Chrome or Edge. No installation is needed to view the dashboard.

## Optional script
`python model_comparison.py` uses only Python's standard library.
`mlflow_tracking.py` is optional and requires MLflow to be installed separately.

## Conclusion
The illustrative comparison selects v1.2 for further validation. Confirm results on a real held-out dataset before making a production decision.
