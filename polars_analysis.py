import polars as pl
import time

# ==========================================
# 1. LOAD DATASET
# ==========================================

csv_file = "student_performance.csv"

print("=" * 60)
print("POLARS ANALYSIS")
print("=" * 60)

start = time.perf_counter()

df = pl.read_csv(csv_file)

load_time = time.perf_counter() - start

print("\nDataset Information")
print("-" * 60)
print("CSV File:", csv_file)
print("Total Rows:", df.height)
print("Total Columns:", df.width)
print("Load Time:", round(load_time, 4), "seconds")


# ==========================================
# QUERY 1
# Average salary by branch
# ==========================================

print("\n" + "=" * 60)
print("QUERY 1: Average Salary by Branch")
print("=" * 60)

start = time.perf_counter()

query1 = (
    df.group_by("branch")
    .agg(
        pl.col("salary_package_lpa")
        .mean()
        .round(2)
        .alias("avg_salary")
    )
    .sort("avg_salary", descending=True)
)

time1 = time.perf_counter() - start

print(query1)
print("\nExecution Time:", round(time1, 4), "seconds")

query1.write_csv("polars_query1.csv")


# ==========================================
# QUERY 2
# Average CGPA by college tier
# ==========================================

print("\n" + "=" * 60)
print("QUERY 2: Average CGPA by College Tier")
print("=" * 60)

start = time.perf_counter()

query2 = (
    df.group_by("college_tier")
    .agg(
        pl.col("cgpa")
        .mean()
        .round(2)
        .alias("avg_cgpa")
    )
    .sort("avg_cgpa", descending=True)
)

time2 = time.perf_counter() - start

print(query2)
print("\nExecution Time:", round(time2, 4), "seconds")

query2.write_csv("polars_query2.csv")


# ==========================================
# QUERY 3
# Placement Status Count
# ==========================================

print("\n" + "=" * 60)
print("QUERY 3: Placement Status Count")
print("=" * 60)

start = time.perf_counter()

query3 = (
    df.group_by("placement_status")
    .agg(
        pl.len().alias("total_students")
    )
    .sort("total_students", descending=True)
)

time3 = time.perf_counter() - start

print(query3)
print("\nExecution Time:", round(time3, 4), "seconds")

query3.write_csv("polars_query3.csv")


# ==========================================
# QUERY 4
# Average Coding Skills by Branch
# ==========================================

print("\n" + "=" * 60)
print("QUERY 4: Average Coding Skills by Branch")
print("=" * 60)

start = time.perf_counter()

query4 = (
    df.group_by("branch")
    .agg(
        pl.col("coding_skills")
        .mean()
        .round(2)
        .alias("avg_coding_skills")
    )
    .sort("avg_coding_skills", descending=True)
)

time4 = time.perf_counter() - start

print(query4)
print("\nExecution Time:", round(time4, 4), "seconds")

query4.write_csv("polars_query4.csv")


# ==========================================
# QUERY 5
# Top 10 Highest Salary Packages
# ==========================================

print("\n" + "=" * 60)
print("QUERY 5: Top 10 Highest Salary Packages")
print("=" * 60)

start = time.perf_counter()

query5 = (
    df.sort(
        "salary_package_lpa",
        descending=True
    )
    .head(10)
)

time5 = time.perf_counter() - start

print(query5)
print("\nExecution Time:", round(time5, 4), "seconds")

query5.write_csv("polars_query5.csv")


# ==========================================
# BENCHMARK SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("POLARS BENCHMARK SUMMARY")
print("=" * 60)

print(f"Query 1 - Average salary by branch:       {time1:.4f} seconds")
print(f"Query 2 - Average CGPA by college tier:   {time2:.4f} seconds")
print(f"Query 3 - Placement status count:         {time3:.4f} seconds")
print(f"Query 4 - Coding skills by branch:        {time4:.4f} seconds")
print(f"Query 5 - Top 10 salary packages:         {time5:.4f} seconds")

total_time = time1 + time2 + time3 + time4 + time5

print("-" * 60)
print(f"Total query execution time:               {total_time:.4f} seconds")

print("\nAnalysis completed successfully!")