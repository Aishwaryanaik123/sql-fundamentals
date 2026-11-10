import csv
from collections import defaultdict
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"data"/"sales_performance_synthetic.csv"
years=defaultdict(float); regions=defaultdict(float); products=defaultdict(float)
with p.open(encoding="utf-8",newline="") as f:
 for r in csv.DictReader(f):
  years[int(r["year"])]+=float(r["sales"]); regions[r["region"]]+=float(r["sales"]); products[r["product"]]+=float(r["sales"])
print("Annual totals:",dict(sorted(years.items())))
print("Regional totals:",dict(sorted(regions.items())))
print("Product totals:",dict(sorted(products.items())))
