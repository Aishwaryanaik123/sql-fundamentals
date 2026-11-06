# Week 9 Day 1 — MLflow Model Registry for Analyst Models

**Task:** MLflow Model Registry for Analyst Models

## Objective
Demonstrate how an analyst can register a trained machine-learning model, create a model version, add useful metadata, and designate a model version for use.

## Project files
- `scripts/model_registry.py` — example workflow for training, logging, registering, and tagging a model.
- `docs/model_registry_notes.md` — explanation of the registry workflow and model lifecycle.
- `WORKLOG.md` — concise record of the work documented for this task.
- `artifacts/` — reserved for outputs generated when the script is run.

## Workflow demonstrated
1. Train a sample classification model.
2. Log model parameters and evaluation metrics to an MLflow run.
3. Register the logged model in the MLflow Model Registry.
4. Add model-version tags and a description.
5. Assign the `Champion` alias to the registered version (where supported).
6. Load the registered model by alias for inference.

## Execution status
This folder contains prepared source code and documentation. MLflow has not been installed or executed while creating this package, so no live registered model or registry version is claimed.

## Suggested commit
`feat: add mlflow model registry for analyst models`
