"""
MLflow tracking for the A/B test.
Uses the MLflow Python API when MLflow is available. No installation is
performed by this project. If MLflow is absent, the script exits with a clear
message; the precomputed analysis artifacts are included in this folder.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load_metrics():
    metrics = {}
    with (ROOT / "analysis_results.csv").open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            value = row["value"]
            if value.lower() in ("true", "false"):
                metrics[row["metric"]] = 1.0 if value.lower() == "true" else 0.0
            else:
                try:
                    metrics[row["metric"]] = float(value)
                except ValueError:
                    pass
    return metrics

def main():
    try:
        import mlflow
    except ImportError:
        print("MLflow is not installed. No package was installed.")
        print("The A/B analysis outputs are already included.")
        print("To create a live MLflow run later, run this script in an environment with MLflow.")
        return

    mlflow.set_experiment("week-9-day-3-ab-test-tracking")
    metrics = load_metrics()
    with mlflow.start_run(run_name="landing-page-variant-comparison"):
        mlflow.log_params({
            "experiment_name": "landing_page_conversion_test",
            "control_variant": "A",
            "treatment_variant": "B",
            "sample_size_per_variant": 1000,
            "significance_level": 0.05,
            "dataset": "ab_test_data.csv (synthetic)"
        })
        for name, value in metrics.items():
            mlflow.log_metric(name, value)
        mlflow.log_artifact(str(ROOT / "ab_test_data.csv"))
        mlflow.log_artifact(str(ROOT / "analysis_results.csv"))
        mlflow.log_artifact(str(ROOT / "experiment_summary.txt"))
        print("A/B test parameters, metrics, and artifacts logged to MLflow.")
        print("Run `mlflow ui` in this environment to inspect the experiment.")

if __name__ == "__main__":
    main()
