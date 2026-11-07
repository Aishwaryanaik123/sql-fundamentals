# Experiment Process — Week 10 Day 3

## 1. Data preparation
Created a reproducible synthetic transaction-style dataset with 1,200 rows and five numeric features: transaction amount, transaction count in 24 hours, account age, transaction hour, and distance from usual location. Thirty-six rows (3%) were deliberately generated with unusual combinations. A fixed random seed makes the dataset reproducible.

## 2. Data quality and feature selection
Checked the dataset structure and used the five numeric columns as model inputs. The planted evaluation label (`known_injected_anomaly`) was deliberately excluded from all detection features to avoid target leakage.

## 3. Statistical detection
- Z-score: calculated standardized values and flagged a row if any feature had an absolute Z-score of at least 3.
- IQR: calculated first and third quartiles and flagged a row if any feature was outside the 1.5×IQR fences.

## 4. Machine-learning detection
Trained an Isolation Forest with 200 estimators, contamination set to 0.03, and random state 42. The model is unsupervised; planted labels were used only after prediction to calculate demonstration metrics.

## 5. Combined decision and evaluation
Created a consensus flag when at least two of the three detection methods agreed. Compared each method with the planted evaluation labels using precision, recall, F1-score, and number of flagged records.

## 6. Outputs
Saved row-level flags, a method comparison CSV, charts, and a standalone HTML report under `reports/`.

## 7. Interpretation
IQR identified every planted anomaly but also flagged more normal records. Z-score and Isolation Forest matched the planted anomalies in this controlled dataset. The combined vote retained the planted cases. These outcomes are specific to this deliberately separated synthetic dataset and should not be generalized to real-world data.
