"""Train baseline models and track each run with MLflow."""
from __future__ import annotations

import json
import time
from pathlib import Path

import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    f1_score, precision_score, recall_score, roc_auc_score,
)
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "customer_activity.csv"
EXPERIMENT_NAME = "tracked-da-experiment-pipeline"
RANDOM_STATE = 42
TEST_SIZE = 0.25


def evaluate_and_log(model, model_name: str, X_train, X_test, y_train, y_test):
    with mlflow.start_run(run_name=model_name):
        mlflow.set_tags({
            "pipeline_version": "1.0",
            "dataset": "customer_activity.csv",
            "experiment_purpose": "baseline churn classification",
        })
        mlflow.log_params({
            "model_name": model_name,
            "test_size": TEST_SIZE,
            "random_state": RANDOM_STATE,
            "feature_count": X_train.shape[1],
            "train_rows": len(X_train),
            "test_rows": len(X_test),
        })

        start = time.perf_counter()
        model.fit(X_train, y_train)
        training_seconds = time.perf_counter() - start

        predictions = model.predict(X_test)
        probabilities = model.predict_proba(X_test)[:, 1]
        metrics = {
            "accuracy": accuracy_score(y_test, predictions),
            "precision": precision_score(y_test, predictions, zero_division=0),
            "recall": recall_score(y_test, predictions, zero_division=0),
            "f1_score": f1_score(y_test, predictions, zero_division=0),
            "roc_auc": roc_auc_score(y_test, probabilities),
            "training_seconds": training_seconds,
        }
        mlflow.log_metrics({key: float(value) for key, value in metrics.items()})

        artifact_dir = ROOT / "reports" / f"run_{model_name.lower().replace(' ', '_')}"
        artifact_dir.mkdir(parents=True, exist_ok=True)
        (artifact_dir / "evaluation.json").write_text(
            json.dumps(metrics, indent=2), encoding="utf-8"
        )
        (artifact_dir / "classification_report.txt").write_text(
            classification_report(y_test, predictions, zero_division=0),
            encoding="utf-8",
        )

        matrix = confusion_matrix(y_test, predictions)
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.imshow(matrix)
        ax.set_title(f"Confusion Matrix – {model_name}")
        ax.set_xlabel("Predicted")
        ax.set_ylabel("Actual")
        for (row, col), value in __import__("numpy").ndenumerate(matrix):
            ax.text(col, row, str(value), ha="center", va="center")
        fig.tight_layout()
        image_path = artifact_dir / "confusion_matrix.png"
        fig.savefig(image_path, dpi=140)
        plt.close(fig)

        mlflow.log_artifacts(str(artifact_dir), artifact_path="evaluation")
        mlflow.log_artifact(str(DATA_PATH), artifact_path="dataset")
        mlflow.sklearn.log_model(model, artifact_path="model")
        print(f"{model_name}: " + ", ".join(
            f"{key}={value:.4f}" for key, value in metrics.items()
        ))


def main():
    data = pd.read_csv(DATA_PATH)
    target = data["churn"]
    features = data.drop(columns=["customer_id", "churn"])
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=TEST_SIZE,
        random_state=RANDOM_STATE, stratify=target,
    )

    mlflow.set_experiment(EXPERIMENT_NAME)
    candidates = [
        ("Logistic Regression", LogisticRegression(max_iter=1000)),
        ("Random Forest", RandomForestClassifier(
            n_estimators=150, max_depth=6, random_state=RANDOM_STATE,
            class_weight="balanced",
        )),
    ]
    for name, estimator in candidates:
        evaluate_and_log(estimator, name, X_train, X_test, y_train, y_test)

    print(f"\nExperiment complete: {EXPERIMENT_NAME}")
    print("Start the UI with: mlflow ui")


if __name__ == "__main__":
    main()
