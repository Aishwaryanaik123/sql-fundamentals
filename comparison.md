\# Pandas vs DuckDB vs Polars Comparison



\## Benchmark Results



The following benchmark was performed using the same 100,000-row

student performance CSV dataset.



| Operation | Pandas | DuckDB | Polars |

|---|---:|---:|---:|

| Count Rows | 0.000008 s | 0.010756 s | 0.000004 s |

| Average CGPA | 0.000492 s | 0.009042 s | 0.002443 s |

| Salary by Branch | 0.010812 s | 0.016874 s | 0.006859 s |

| Placement Status | 0.001658 s | 0.024351 s | 0.001870 s |

| Salary by College Tier | 0.010797 s | 0.016855 s | 0.002169 s |



\## Tool Comparison



| Criteria | Pandas | DuckDB | Polars |

|---|---|---|---|

| Main interface | Python/DataFrame | SQL | Python/DataFrame |

| Query syntax | Python | SQL | Python expressions |

| CSV/Parquet analytics | Good | Excellent | Excellent |

| Performance | Good | Good for analytical SQL | High performance |

| Best suited for | General data analysis | SQL-based analytics | Fast DataFrame processing |



\## Syntax Comparison



| Operation | Pandas | DuckDB | Polars |

|---|---|---|---|

| Load CSV | `pd.read\_csv()` | `read\_csv\_auto()` / SQL | `pl.read\_csv()` |

| Filter | DataFrame filtering | `WHERE` | `filter()` |

| Group By | `groupby()` | `GROUP BY` | `group\_by()` |

| Average | `.mean()` | `AVG()` | `.mean()` |

| Sort | `.sort\_values()` | `ORDER BY` | `.sort()` |



\## Conclusion



Pandas provides a simple and flexible Python-based approach for

data analysis. DuckDB allows analytical queries to be written using

SQL and is useful for SQL-based data analysis. Polars provides a

high-performance DataFrame API and showed strong performance in the

benchmark operations.



The benchmark results are specific to this execution environment

and may vary between runs.

