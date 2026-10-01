\# Automated EDA - Week 5 Day 4



\## Task



Performance comparison of Pandas, DuckDB, and Polars using a 100,000-row student performance dataset.



\## Dataset



\- File: `student\_performance.csv`

\- Rows: 100,000

\- Columns: 18



\## Tools Used



\- Python

\- Pandas

\- DuckDB

\- Polars

\- VS Code

\- Git

\- GitHub



\## Analysis Performed



1\. Loaded the 100k-row CSV into DuckDB.

2\. Ran 5 analytical SQL queries.

3\. Benchmarked DuckDB against Pandas.

4\. Loaded the same dataset into Polars.

5\. Ran the same 5 analytical operations.

6\. Compared Pandas, DuckDB, and Polars.



\## Queries



1\. Average salary by branch

2\. Average CGPA by college tier

3\. Placement status count

4\. Average coding skills by branch

5\. Top 10 highest salary packages



\## Benchmark Results



| Tool | Total Query Time |

|---|---:|

| Pandas | 0.0824 seconds |

| Polars | 0.1282 seconds |

| DuckDB | 0.8670 seconds |



\## Files



\- `student\_performance.csv` - Dataset

\- `duckdb\_analysis.py` - DuckDB analysis

\- `pandas\_analysis.py` - Pandas analysis

\- `polars\_analysis.py` - Polars analysis

\- Query result CSV files

\- `README.md` - Project documentation



\## Conclusion



The three tools were tested using the same dataset and analytical operations. In this particular benchmark, Pandas had the lowest total query execution time, followed by Polars and DuckDB.

