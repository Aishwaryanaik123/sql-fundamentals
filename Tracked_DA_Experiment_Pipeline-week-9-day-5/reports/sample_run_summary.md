# Sample Experiment Summary

**Status:** Illustrative report – not generated from a live MLflow run.

| Candidate | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.82 | 0.79 | 0.76 | 0.77 | 0.86 |
| Random Forest | 0.86 | 0.84 | 0.81 | 0.82 | 0.90 |

## Interpretation
In this illustrative example, Random Forest has the stronger F1 and ROC-AUC values. The conclusion is not hard-coded into the pipeline: after execution, `compare_runs.py` ranks the actual tracked runs by F1 score.

## Recommendation
Treat Random Forest as the example candidate for further validation only. Confirm performance using real, approved data, cross-validation, and business-relevant error analysis before deployment.
