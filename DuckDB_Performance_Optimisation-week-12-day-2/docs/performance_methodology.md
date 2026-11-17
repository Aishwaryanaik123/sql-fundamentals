# Performance comparison methodology

- Dataset: 100,000 synthetic sales rows, generated with a fixed random seed for repeatability.
- Engines: Pandas groupby aggregations and DuckDB SQL aggregations over the same CSV data.
- Comparisons: region sales/profit, category sales/profit, and monthly sales.
- Each query is warmed up once, then measured five times using `time.perf_counter`; the median is reported.
- The benchmark records local machine timings in `reports/benchmark_results.csv`. Results vary with CPU, memory, disk, Python, Pandas, and DuckDB versions.
- DuckDB is tested as an in-process analytical engine. The reusable query helper caches results by exact SQL string in an LRU cache (maximum 128 entries). Call `clear_query_cache()` after changing source data.
- No benchmark speedup is claimed in advance: run the benchmark locally to produce measured results.
