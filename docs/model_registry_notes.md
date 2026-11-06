# MLflow Model Registry — Notes

## What is the Model Registry?
The MLflow Model Registry is a centralized place to manage the lifecycle of machine-learning models. It records registered model names, versions, metadata, and references to the logged model artifacts.

## Main concepts
- **Registered model:** A named model entry in the registry.
- **Model version:** A specific version of a registered model. New registrations create new versions.
- **Tags and description:** Metadata that explains ownership, purpose, or evaluation context.
- **Alias:** A mutable name such as `Champion` that points to a particular model version. Aliases are preferred over the older fixed stage workflow in current MLflow versions.

## Process in this example
1. Load a sample dataset and split it into training and test data.
2. Train a Random Forest classifier.
3. Calculate accuracy, precision, recall, and F1-score.
4. Start an MLflow run and log model parameters and metrics.
5. Log the model with a registered model name, which creates a registry version.
6. Add tags and a description to that version.
7. Assign the `Champion` alias to the version, if supported by the installed MLflow version.
8. Load the model from the registry and use it for inference.

## Why analysts use it
The registry helps analysts keep track of which model version was evaluated, preserve model lineage, compare versions, and identify the intended model for downstream use.

## Important note
This project is a code-and-documentation example. No registry database, live model version, or execution output was generated during packaging.
