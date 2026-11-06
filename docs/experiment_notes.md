# Experiment Notes

## Purpose
MLflow Tracking provides a central place to record machine-learning experiment runs. It makes it easier to reproduce experiments and compare model configurations.

## Workflow
1. Select or create an MLflow experiment named `Week-9-Day-1-DA-Experiments`.
2. Load a sample classification dataset.
3. Split the data into training and testing sets.
4. Train three model configurations.
5. Start a separate MLflow run for each model.
6. Log run parameters and evaluation metrics.
7. Log the trained model and a CSV comparison artifact.
8. Compare runs in the MLflow UI.

## Logged parameters
- Model name
- Test dataset proportion
- Random seed
- Dataset name

## Logged metrics
- Accuracy
- Precision
- Recall
- F1-score

## Artifacts
- Trained model for each run
- `run_metrics.csv` comparison table

## Interpretation
Each run is stored separately under the same experiment. The MLflow UI can display the logged parameters and metrics side by side. This helps an analyst identify which model performed better on the selected evaluation metrics.

## Result status
The project code and documentation are prepared. No live MLflow run was generated while packaging this folder; the metrics CSV is created by the script when it is executed in an MLflow-enabled Python environment.
