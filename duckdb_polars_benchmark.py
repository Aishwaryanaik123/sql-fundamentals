import pandas as pd
import duckdb
import polars as pl
import time

# Load the 100k-row CSV
csv_file = "student_performance.csv"

df = pd.read_csv(csv_file)

print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Create DuckDB connection
con = duckdb.connect()

print("DuckDB connected successfully!")


# Query 1: Count total rows
result = con.execute("""
    SELECT COUNT(*) AS total_rows
    FROM df
""").fetchdf()

print("\nQuery 1 - Total Rows")
print(result)


# Query 2: Average CGPA
result = con.execute("""
    SELECT AVG(cgpa) AS average_cgpa
    FROM df
""").fetchdf()

print("\nQuery 2 - Average CGPA")
print(result)


# Query 3: Average salary by branch
result = con.execute("""
    SELECT
        branch,
        AVG(salary_package_lpa) AS average_salary
    FROM df
    GROUP BY branch
    ORDER BY average_salary DESC
""").fetchdf()

print("\nQuery 3 - Average Salary by Branch")
print(result)


# Query 4: Placement status count
result = con.execute("""
    SELECT
        placement_status,
        COUNT(*) AS student_count
    FROM df
    GROUP BY placement_status
""").fetchdf()

print("\nQuery 4 - Placement Status")
print(result)


# Query 5: Average salary by college tier
result = con.execute("""
    SELECT
        college_tier,
        AVG(salary_package_lpa) AS average_salary
    FROM df
    GROUP BY college_tier
    ORDER BY college_tier
""").fetchdf()

print("\nQuery 5 - Average Salary by College Tier")
print(result)


# =========================
# DuckDB Benchmark
# =========================

duckdb_times = {}

start = time.perf_counter()

con.execute("""
    SELECT COUNT(*) FROM df
""").fetchdf()

duckdb_times["Count Rows"] = time.perf_counter() - start


start = time.perf_counter()

con.execute("""
    SELECT AVG(cgpa) FROM df
""").fetchdf()

duckdb_times["Average CGPA"] = time.perf_counter() - start


start = time.perf_counter()

con.execute("""
    SELECT branch, AVG(salary_package_lpa)
    FROM df
    GROUP BY branch
""").fetchdf()

duckdb_times["Salary by Branch"] = time.perf_counter() - start


start = time.perf_counter()

con.execute("""
    SELECT placement_status, COUNT(*)
    FROM df
    GROUP BY placement_status
""").fetchdf()

duckdb_times["Placement Status"] = time.perf_counter() - start


start = time.perf_counter()

con.execute("""
    SELECT college_tier, AVG(salary_package_lpa)
    FROM df
    GROUP BY college_tier
""").fetchdf()

duckdb_times["Salary by College Tier"] = time.perf_counter() - start


print("\n===== DuckDB Benchmark =====")

for operation, duration in duckdb_times.items():
    print(f"{operation}: {duration:.6f} seconds")



# =========================
# Pandas Benchmark
# =========================

pandas_times = {}

start = time.perf_counter()

len(df)

pandas_times["Count Rows"] = time.perf_counter() - start


start = time.perf_counter()

df["cgpa"].mean()

pandas_times["Average CGPA"] = time.perf_counter() - start


start = time.perf_counter()

df.groupby("branch")["salary_package_lpa"].mean()

pandas_times["Salary by Branch"] = time.perf_counter() - start


start = time.perf_counter()

df["placement_status"].value_counts()

pandas_times["Placement Status"] = time.perf_counter() - start


start = time.perf_counter()

df.groupby("college_tier")["salary_package_lpa"].mean()

pandas_times["Salary by College Tier"] = time.perf_counter() - start


print("\n===== Pandas Benchmark =====")

for operation, duration in pandas_times.items():
    print(f"{operation}: {duration:.6f} seconds")  


# =========================
# Load dataset using Polars
# =========================

polars_df = pl.read_csv(csv_file)

print("\n===== Polars Dataset =====")
print("Rows:", polars_df.height)
print("Columns:", polars_df.width)    



# =========================
# Polars Benchmark
# =========================

polars_times = {}

# 1. Count Rows
start = time.perf_counter()

polars_df.height

polars_times["Count Rows"] = time.perf_counter() - start


# 2. Average CGPA
start = time.perf_counter()

polars_df.select(
    pl.col("cgpa").mean()
)

polars_times["Average CGPA"] = time.perf_counter() - start


# 3. Average Salary by Branch
start = time.perf_counter()

polars_df.group_by("branch").agg(
    pl.col("salary_package_lpa").mean()
)

polars_times["Salary by Branch"] = time.perf_counter() - start


# 4. Placement Status
start = time.perf_counter()

polars_df.group_by("placement_status").len()

polars_times["Placement Status"] = time.perf_counter() - start


# 5. Average Salary by College Tier
start = time.perf_counter()

polars_df.group_by("college_tier").agg(
    pl.col("salary_package_lpa").mean()
)

polars_times["Salary by College Tier"] = time.perf_counter() - start


print("\n===== Polars Benchmark =====")

for operation, duration in polars_times.items():
    print(f"{operation}: {duration:.6f} seconds")