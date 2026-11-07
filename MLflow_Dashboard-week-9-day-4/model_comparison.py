"""Compare illustrative model-version metrics using Python's standard library."""
import csv
from pathlib import Path

path = Path(__file__).with_name("model_versions.csv")
with path.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

if not rows:
    raise SystemExit("No comparison rows found.")

metrics = ["accuracy", "precision", "recall", "f1_score", "roc_auc"]
print("MLFLOW DASHBOARD – MODEL VERSION COMPARISON")
print("=" * 48)
for row in rows:
    values = ", ".join(f"{m}={float(row[m]):.3f}" for m in metrics)
    print(f'{row["model_version"]}: {values}, training_time={float(row["training_time_seconds"]):.1f}s')

best = max(rows, key=lambda r: float(r["f1_score"]))
first, last = rows[0], rows[-1]
gain = (float(last["accuracy"]) - float(first["accuracy"])) * 100
time_gain = float(last["training_time_seconds"]) - float(first["training_time_seconds"])
print("-" * 48)
print(f'Best version by F1 score: {best["model_version"]}')
print(f"Accuracy change: {gain:.1f} percentage points")
print(f"Training-time change: {time_gain:.1f} seconds")
print("NOTE: Demonstration values only; not measured model results.")
