# Week 9 Day 1 — MLflow Tracking: Log DA Experiments

**Programme:** Data Analyst Intern 3M  
**Task:** MLflow Tracking — Log DA Experiments

## Objective
Demonstrate how a data analyst can use MLflow Tracking to record experiment parameters, evaluation metrics, and output artifacts, then compare multiple experiment runs.

## Project contents
- `scripts/mlflow_tracking.py` — complete example that creates an MLflow experiment and logs three model runs.
- `data/experiment_data.csv` — small illustrative dataset used by the example.
- `artifacts/` — contains a sample comparison table for documentation purposes.
- `docs/experiment_notes.md` — workflow, observations, and interpretation.
- `WORKLOG.md` — task documentation.

## What the script demonstrates
1. Creates or selects an MLflow experiment.
2. Starts separate runs for three model configurations.
3. Logs parameters such as model name, test size, and random seed.
4. Logs metrics such as accuracy, precision, recall, and F1-score.
5. Saves and logs a metrics CSV artifact.
6. Uses the MLflow UI to review and compare runs.

## Important execution note
This submission folder is prepared as source code and documentation. MLflow has **not** been installed or executed as part of creating this folder. To generate live MLflow run records on a computer, Python and the `mlflow` package are required. No installation or execution is required just to review or submit these project files.

## Suggested commit message
`feat: complete week-9-day-1 mlflow experiment tracking`
