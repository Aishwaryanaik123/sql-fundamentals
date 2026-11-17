# Performance Optimisation — DuckDB + Query Caching

**Data Analyst Intern 3M | Week 12 Day 2**

## Objective
Load a 100k-row CSV into DuckDB, run analytical SQL, compare DuckDB with Pandas, and provide a reusable SQL-to-Pandas function with query-result caching.

## Project contents
- `data/sales_100k.csv` — 100,000-row reproducible synthetic sales dataset.
- `sql/analytical_queries.sql` — five analytical SQL queries.
- `src/duckdb_utils.py` — reusable `query_to_df(sql)` function and LRU result cache.
- `src/run_analysis.py` — initializes the DuckDB database, runs five queries, and exports CSV results.
- `src/benchmark_pandas_vs_duckdb.py` — compares three equivalent queries and records median timings.
- `docs/performance_methodology.md` — benchmark method and interpretation notes.

## Run on Windows PowerShell
From this project folder:

```powershell
py -m pip install -r requirements.txt
py src\run_analysis.py
py src\benchmark_pandas_vs_duckdb.py
```

The first script creates `data/sales_analytics.duckdb` and writes five query outputs under `reports/`. The benchmark writes `reports/benchmark_results.csv`.

## Reusable function
```python
from src.duckdb_utils import query_to_df
result = query_to_df("SELECT region, SUM(sales) AS total_sales FROM sales GROUP BY region")
print(result)
```

The helper returns a Pandas DataFrame. Repeated identical SQL strings use the in-memory LRU cache. Call `clear_query_cache()` after changing the underlying table.

## Benchmark interpretation
The benchmark warms up each query, measures five runs, and reports the median time. A speedup above 1.0 means DuckDB was faster for that measured query on the machine used. Timings depend on hardware and software versions; do not compare results across machines as if they were controlled experiments.

## Data and limitations
The dataset is synthetic and intended for learning, not real business conclusions. DuckDB execution and timing results must be generated on the target computer after installing the requirements. No unmeasured speedup is claimed.
