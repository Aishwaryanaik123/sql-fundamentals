"""Compare three equivalent analytical queries in Pandas and DuckDB.
Run after installing requirements.txt. Times are measured on your machine.
"""
from pathlib import Path
import sys, time, statistics
import pandas as pd
import duckdb
ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "data" / "sales_100k.csv"
OUT = ROOT / "reports" / "benchmark_results.csv"

df = pd.read_csv(CSV, parse_dates=["order_date"])
con = duckdb.connect()
con.execute("CREATE TABLE sales AS SELECT * FROM read_csv_auto(?)", [str(CSV)])

queries = {
 "region_sales": (
  lambda: df.groupby("region", as_index=False).agg(total_sales=("sales","sum"), total_profit=("profit","sum")).sort_values("total_sales", ascending=False).reset_index(drop=True),
  "SELECT region, SUM(sales) AS total_sales, SUM(profit) AS total_profit FROM sales GROUP BY region ORDER BY total_sales DESC"),
 "category_sales": (
  lambda: df.groupby("category", as_index=False).agg(order_lines=("order_id","count"), total_sales=("sales","sum"), total_profit=("profit","sum")).sort_values("total_sales", ascending=False).reset_index(drop=True),
  "SELECT category, COUNT(order_id) AS order_lines, SUM(sales) AS total_sales, SUM(profit) AS total_profit FROM sales GROUP BY category ORDER BY total_sales DESC"),
 "monthly_sales": (
  lambda: df.assign(sales_month=df["order_date"].dt.to_period("M").dt.to_timestamp()).groupby("sales_month", as_index=False).agg(monthly_sales=("sales","sum")).sort_values("sales_month").reset_index(drop=True),
  "SELECT DATE_TRUNC('month', CAST(order_date AS DATE)) AS sales_month, SUM(sales) AS monthly_sales FROM sales GROUP BY 1 ORDER BY 1")
}

def median_seconds(fn, repeats=5):
    fn()  # warm-up, excluded from timing
    samples=[]
    for _ in range(repeats):
        t=time.perf_counter(); fn(); samples.append(time.perf_counter()-t)
    return statistics.median(samples)

rows=[]
for name,(pandas_fn,sql) in queries.items():
    p=median_seconds(pandas_fn); d=median_seconds(lambda: con.execute(sql).fetchdf())
    rows.append({"query":name,"pandas_median_seconds":round(p,6),"duckdb_median_seconds":round(d,6),"duckdb_speedup_vs_pandas":round(p/d,3) if d else None,"repeats":5})
    print(f"{name}: Pandas={p:.6f}s | DuckDB={d:.6f}s | speedup={p/d:.2f}x")
OUT.parent.mkdir(exist_ok=True); pd.DataFrame(rows).to_csv(OUT,index=False)
print(f"\nSaved actual benchmark measurements to {OUT}")
con.close()
