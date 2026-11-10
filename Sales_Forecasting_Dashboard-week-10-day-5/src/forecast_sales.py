"""Rebuild the Week 10 Day 5 sales forecasting outputs using Python standard library."""
import csv, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / "data" / "monthly_sales.csv").open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
for r in rows:
    r["year"], r["month"], r["sales"] = int(r["year"]), int(r["month"]), float(r["sales"])

def fit(data):
    X, y = [], []
    for i, r in enumerate(data):
        X.append([1.0, float(i)] + [1.0 if r["month"] == m else 0.0 for m in range(2, 13)])
        y.append(r["sales"])
    p = len(X)
    A = [[sum(X[k][i]*X[k][j] for k in range(len(X))) for j in range(p)] for i in range(p)]
    b = [sum(X[k][i]*y[k] for k in range(len(X))) for i in range(p)]
    for col in range(p):
        pivot = max(range(col,p), key=lambda r: abs(A[r][col]))
        A[col], A[pivot] = A[pivot], A[col]
        b[col], b[pivot] = b[pivot], b[col]
        div = A[col][col]
        for j in range(col,p): A[col][j] /= div
        b[col] /= div
        for r in range(p):
            if r == col: continue
            factor = A[r][col]
            for j in range(col,p): A[r][j] -= factor*A[col][j]
            b[r] -= factor*b[col]
    return b

def predict(c, idx, month):
    x = [1.0, float(idx)] + [1.0 if month == m else 0.0 for m in range(2,13)]
    return sum(a*b for a,b in zip(c,x))

train, test = rows[:-12], rows[-12:]
c = fit(train)
errors = []
for j, r in enumerate(test):
    errors.append((r["sales"], predict(c, len(train)+j, r["month"])))
mae = sum(abs(a-p) for a,p in errors)/len(errors)
rmse = math.sqrt(sum((a-p)**2 for a,p in errors)/len(errors))
print(f"Holdout MAE: {mae:.2f}; RMSE: {rmse:.2f}")
c = fit(rows)
out = ROOT / "reports" / "12_month_sales_forecast.csv"
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["date","year","month","forecast_sales","lower_estimate","upper_estimate"])
    for h in range(12):
        idx = len(rows)+h; month = idx%12+1; year = 2019+idx//12
        pred = max(0,predict(c,idx,month))
        w.writerow([f"{year}-{month:02d}-01",year,month,round(pred,2),round(max(0,pred-1.5*rmse),2),round(pred+1.5*rmse,2)])
print(f"Saved forecast to {out}")
