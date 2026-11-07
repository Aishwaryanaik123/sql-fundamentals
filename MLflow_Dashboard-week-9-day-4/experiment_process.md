# Experiment Process Documentation

## 1. Objective
Compare model versions v1.0, v1.1, and v1.2 using accuracy, precision, recall, F1 score, ROC-AUC, and training time.

## 2. Workflow
1. Define the versions to compare.
2. Collect the same evaluation metrics for every version.
3. Store results in `model_versions.csv`.
4. Compare predictive performance and training cost.
5. Present results in `dashboard.html`.
6. Document the best candidate and trade-offs.
7. For a live MLflow experiment, log one run per version under a shared experiment.

## 3. Results
v1.2 has the highest accuracy (0.873), precision (0.866), recall (0.845), F1 score (0.855), and ROC-AUC (0.914). Its training time is 22.7 seconds versus 18.4 seconds for v1.0.

Accuracy improves by 3.1 percentage points from v1.0 to v1.2, while training time increases by 4.3 seconds.

## 4. Recommendation
Select v1.2 for further validation because it leads on all reported predictive metrics. Before deployment, repeat the comparison on a common held-out dataset with consistent preprocessing and evaluation conditions.

## 5. MLflow dashboard mapping
For a real MLflow run:
- Experiment name: `week-9-day-4-model-version-comparison`
- Create one run per model version.
- Log `model_version` as a parameter.
- Log accuracy, precision, recall, F1, ROC-AUC, and training time as metrics.
- Log the evaluation CSV and plots as artifacts.
- Compare runs in the MLflow experiment Runs table.

## 6. Limitations
The values are illustrative, not measurements from trained models. No live MLflow server or tracking run was started. The included HTML is an offline comparison report, not a live MLflow UI.
