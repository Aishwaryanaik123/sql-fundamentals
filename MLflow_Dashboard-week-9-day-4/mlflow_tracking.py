"""Optional example: log the illustrative CSV values to MLflow.
Requires MLflow to be installed. This does not train or evaluate models.
"""
import csv
from pathlib import Path
import mlflow

csv_path = Path(__file__).with_name("model_versions.csv")
mlflow.set_experiment("week-9-day-4-model-version-comparison")
with csv_path.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        with mlflow.start_run(run_name=row["model_version"]):
            mlflow.log_param("model_version", row["model_version"])
            mlflow.log_param("notes", row["notes"])
            for key in ("accuracy", "precision", "recall", "f1_score", "roc_auc", "training_time_seconds"):
                mlflow.log_metric(key, float(row[key]))
            mlflow.log_artifact(str(csv_path))
print("Logged illustrative comparison values. These are not trained-model results.")
