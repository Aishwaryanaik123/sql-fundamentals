"""Compare MLflow runs for the Week 9 Day 5 experiment."""
import mlflow
import pandas as pd

EXPERIMENT_NAME = "tracked-da-experiment-pipeline"


def main():
    experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
    if experiment is None:
        raise SystemExit(
            f"No experiment named {EXPERIMENT_NAME!r}. Run train_experiment.py first."
        )

    runs = mlflow.search_runs(
        experiment_ids=[experiment.experiment_id],
        order_by=["metrics.f1_score DESC"],
    )
    if runs.empty:
        raise SystemExit("No completed runs found. Run train_experiment.py first.")

    columns = [
        "tags.mlflow.runName", "params.model_name",
        "metrics.accuracy", "metrics.precision", "metrics.recall",
        "metrics.f1_score", "metrics.roc_auc", "metrics.training_seconds",
    ]
    available = [column for column in columns if column in runs.columns]
    print(runs[available].to_string(index=False))
    winner = runs.iloc[0]
    print(
        "\nTop run by F1 score: "
        f"{winner.get('params.model_name', winner.get('tags.mlflow.runName'))} "
        f"(F1={winner.get('metrics.f1_score', float('nan')):.4f})"
    )


if __name__ == "__main__":
    main()
