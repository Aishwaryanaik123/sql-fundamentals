"""
Week 9 Day 1: MLflow Model Registry for Analyst Models

Demonstrates training a model, logging it to MLflow, registering it,
adding metadata, assigning an alias, and loading the registered model.

Requires an environment with mlflow, pandas, and scikit-learn installed.
No external dataset download is needed; a scikit-learn sample dataset is used.
"""

from pathlib import Path

import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_NAME = "Analyst_Breast_Cancer_Classifier"
DATABASE_URI = f"sqlite:///{(PROJECT_ROOT / 'mlflow_registry.db').as_posix()}"

# Use a local SQLite database for tracking and registry metadata.
mlflow.set_tracking_uri(DATABASE_URI)
mlflow.set_registry_uri(DATABASE_URI)
mlflow.set_experiment("Week-9-Day-1-Model-Registry")

# Load a built-in dataset (no manual data file or download required).
dataset = load_breast_cancer(as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(
    dataset.data,
    dataset.target,
    test_size=0.20,
    random_state=42,
    stratify=dataset.target,
)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42,
)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

metrics = {
    "accuracy": accuracy_score(y_test, predictions),
    "precision": precision_score(y_test, predictions, zero_division=0),
    "recall": recall_score(y_test, predictions, zero_division=0),
    "f1_score": f1_score(y_test, predictions, zero_division=0),
}

with mlflow.start_run(run_name="random-forest-analyst-model") as run:
    mlflow.log_params({
        "model_type": "RandomForestClassifier",
        "n_estimators": 100,
        "max_depth": 5,
        "test_size": 0.20,
        "random_state": 42,
        "dataset": "sklearn_breast_cancer",
    })
    mlflow.log_metrics(metrics)

    model_info = mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        registered_model_name=MODEL_NAME,
    )
    run_id = run.info.run_id

client = MlflowClient()
versions = client.search_model_versions(f"name='{MODEL_NAME}'")
if not versions:
    raise RuntimeError(f"No registered version found for {MODEL_NAME}")

# Select the version created by this run.
registered_version = next(
    (v for v in versions if v.run_id == run_id),
    versions[0],
)
version_number = registered_version.version

client.set_model_version_tag(MODEL_NAME, version_number, "team", "Data Analytics")
client.set_model_version_tag(MODEL_NAME, version_number, "purpose", "Analyst model evaluation")
client.update_model_version(
    name=MODEL_NAME,
    version=version_number,
    description="Random Forest classification model logged for analyst model registry demonstration.",
)

# Model aliases are the current registry mechanism for naming a preferred version.
try:
    client.set_registered_model_alias(MODEL_NAME, "Champion", version_number)
    print(f"Alias 'Champion' assigned to version {version_number}.")
    champion_uri = f"models:/{MODEL_NAME}@Champion"
    registered_model = mlflow.sklearn.load_model(champion_uri)
    print("Loaded registered model through the Champion alias.")
except (AttributeError, NotImplementedError):
    print("This MLflow version does not support model aliases; use the registered version URI.")
    registered_model = mlflow.sklearn.load_model(f"models:/{MODEL_NAME}/{version_number}")

print(f"Registered model: {MODEL_NAME}")
print(f"Registered version: {version_number}")
print(f"Source run ID: {run_id}")
print("Evaluation metrics:")
for metric_name, metric_value in metrics.items():
    print(f"  {metric_name}: {metric_value:.4f}")
