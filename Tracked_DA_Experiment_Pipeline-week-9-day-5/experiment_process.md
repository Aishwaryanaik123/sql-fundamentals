# Experiment Process – Week 9 Day 5

## 1. Define the experiment
Question: can customer activity features help classify churn in a small demonstration dataset?
Target: `churn` (0 = retained, 1 = churned).
Experiment: `tracked-da-experiment-pipeline`.

## 2. Prepare the data
The pipeline reads `data/customer_activity.csv`, separates the target from the features, and uses a reproducible stratified train/test split. Customer IDs are excluded from model inputs to avoid using an identifier as a predictive feature.

## 3. Train candidate models
Two baseline classifiers are trained:
- Logistic Regression
- Random Forest

Both use the same split and random seed so their evaluation is comparable.

## 4. Evaluate
The pipeline calculates accuracy, precision, recall, F1 score, ROC-AUC, and training duration on the held-out test set. The positive class is churn (1); zero-division cases are handled explicitly.

## 5. Track with MLflow
For each candidate, the pipeline logs:
- Parameters (model name, split size, random seed, and model settings)
- Metrics (the six evaluation values)
- Tags (dataset, experiment purpose, and pipeline version)
- Artifacts (classification report, confusion matrix plot, evaluation JSON, and dataset copy)
- Serialized scikit-learn model

## 6. Compare runs
`src/compare_runs.py` reads runs from the named MLflow experiment, sorts them by F1 score, and prints the tracked metrics and parameters. It does not assume that a particular model will win.

## 7. Reproducibility and limitations
The random seed is fixed. The supplied data is synthetic, not actual customer data. Metrics in the offline HTML report are illustrative examples only and are not claimed as results from a live run. Re-run the pipeline to generate genuine MLflow run records from the included dataset.
