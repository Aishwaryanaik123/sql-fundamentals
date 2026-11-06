"""
Week 9 Day 1: MLflow Tracking — Log DA Experiments

This script demonstrates experiment tracking with MLflow using a small
classification dataset. It logs parameters, metrics, and artifacts for
multiple runs so they can be compared in the MLflow UI.

Run in an environment where mlflow, pandas, and scikit-learn are installed:
    python scripts/mlflow_tracking.py
"""

from pathlib import Path
import tempfile

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = PROJECT_ROOT / "artifacts"
ARTIFACT_DIR.mkdir(exist_ok=True)

# Load a built-in sample dataset; no external dataset download is needed.
dataset = load_breast_cancer(as_frame=True)
X = dataset.data
y = dataset.target

mlflow.set_experiment("Week-9-Day-1-DA-Experiments")

experiment_results = []

model_configs = [
    ("LogisticRegression", LogisticRegression(max_iter=2000), 42),
    ("DecisionTree", DecisionTreeClassifier(max_depth=4, random_state=42), 42),
    ("RandomForest", RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42), 42),
]

for model_name, model, seed in model_configs:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=seed, stratify=y
    )

    with mlflow.start_run(run_name=model_name):
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        metrics = {
            "accuracy": accuracy_score(y_test, predictions),
            "precision": precision_score(y_test, predictions, zero_division=0),
            "recall": recall_score(y_test, predictions, zero_division=0),
            "f1_score": f1_score(y_test, predictions, zero_division=0),
        }

        params = {
            "model_name": model_name,
            "test_size": 0.20,
            "random_state": seed,
            "dataset": "sklearn_breast_cancer",
        }

        mlflow.log_params(params)
        mlflow.log_metrics(metrics)
        mlflow.sklearn.log_model(model, artifact_path="model")

        experiment_results.append({"run_name": model_name, **metrics})

# Save and log a comparison artifact after the individual runs.
results_df = pd.DataFrame(experiment_results)
comparison_path = ARTIFACT_DIR / "run_metrics.csv"
results_df.to_csv(comparison_path, index=False)

with mlflow.start_run(run_name="experiment-comparison-summary"):
    mlflow.log_param("number_of_model_runs", len(experiment_results))
    mlflow.log_artifact(str(comparison_path))

print("Experiment tracking completed.")
print(results_df.to_string(index=False))
print("Open the MLflow UI with: mlflow ui")
