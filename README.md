# Week 9 Day 5 – Tracked DA Experiment Pipeline

## Objective
Build a reproducible data-analysis experiment pipeline that loads a dataset, prepares features, trains two baseline classification models, evaluates them with common metrics, and tracks parameters, metrics, tags, and artifacts with MLflow.

## What is included
- `data/customer_activity.csv` – deterministic synthetic demonstration dataset (300 rows).
- `src/train_experiment.py` – end-to-end experiment pipeline with explicit MLflow logging.
- `src/compare_runs.py` – retrieves and compares completed MLflow runs.
- `reports/experiment_comparison.html` – offline sample comparison dashboard.
- `reports/sample_run_summary.md` – sample findings and interpretation.
- `experiment_process.md` – workflow, tracking design, and reproducibility notes.
- `requirements.txt` – dependencies for running the pipeline.
- `execution_notes.txt` – expected commands and output guidance.

## Important data and execution note
The included dataset is synthetic and generated for demonstration. The sample report contains illustrative example metrics so the folder can be reviewed without installing or running anything. No live MLflow experiment was executed when this package was prepared. Running the scripts locally will create real runs from the included synthetic dataset.

## View without installation
Open `reports/experiment_comparison.html` in Chrome or Edge to view the offline sample comparison. No installation is required to view the report.

## Run the pipeline (optional)
Use Python 3.10 or newer.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python src/train_experiment.py
python src/compare_runs.py
mlflow ui
```

Then open `http://127.0.0.1:5000` to inspect the MLflow experiment UI.

## What gets tracked
Each model run logs:
- Parameters: model type, test size, random seed, and model-specific settings.
- Metrics: accuracy, precision, recall, F1 score, ROC-AUC, and training duration.
- Tags: experiment purpose, dataset name, and pipeline version.
- Artifacts: evaluation summary, classification report, confusion matrix image, and a copy of the dataset.

## Expected outputs
MLflow stores experiment metadata and artifacts in the local `mlruns/` directory by default. `compare_runs.py` prints a ranked comparison table and selects the highest-F1 run.

## Conclusion
This project demonstrates an auditable, repeatable DA experiment workflow. Use real, approved data and validate results on a representative holdout set before making business or production decisions.
