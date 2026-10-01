import pandas as pd
import time

# ==========================================
# 1. LOAD DATASET
# ==========================================

csv_file = "student_performance.csv"

print("=" * 60)
print("PANDAS ANALYSIS")
print("=" * 60)

start = time.perf_counter()

df = pd.read_csv(csv_file)

load_time = time.perf_counter() - start

print("\nDataset Information")
print("-" * 60)
print("CSV File:", csv_file)
print("Total Rows:", len(df))
print("Total Columns:", len(df.columns))
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
    df.groupby("branch")["salary_package_lpa"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
    .reset_index()
)

query1.columns = ["branch", "avg_salary"]

time1 = time.perf_counter() - start

print(query1)
print("\nExecution Time:", round(time1, 4), "seconds")

query1.to_csv("pandas_query1.csv", index=False)


# ==========================================
# QUERY 2
# Average CGPA by college tier
# ==========================================

print("\n" + "=" * 60)
print("QUERY 2: Average CGPA by College Tier")
print("=" * 60)

start = time.perf_counter()

query2 = (
    df.groupby("college_tier")["cgpa"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
    .reset_index()
)

query2.columns = ["college_tier", "avg_cgpa"]

time2 = time.perf_counter() - start

print(query2)
print("\nExecution Time:", round(time2, 4), "seconds")

query2.to_csv("pandas_query2.csv", index=False)


# ==========================================
# QUERY 3
# Placement Status Count
# ==========================================

print("\n" + "=" * 60)
print("QUERY 3: Placement Status Count")
print("=" * 60)

start = time.perf_counter()

query3 = (
    df.groupby("placement_status")
    .size()
    .reset_index(name="total_students")
    .sort_values("total_students", ascending=False)
)

time3 = time.perf_counter() - start

print(query3)
print("\nExecution Time:", round(time3, 4), "seconds")

query3.to_csv("pandas_query3.csv", index=False)


# ==========================================
# QUERY 4
# Average Coding Skills by Branch
# ==========================================

print("\n" + "=" * 60)
print("QUERY 4: Average Coding Skills by Branch")
print("=" * 60)

start = time.perf_counter()

query4 = (
    df.groupby("branch")["coding_skills"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
    .reset_index()
)

query4.columns = ["branch", "avg_coding_skills"]

time4 = time.perf_counter() - start

print(query4)
print("\nExecution Time:", round(time4, 4), "seconds")

query4.to_csv("pandas_query4.csv", index=False)


# ==========================================
# QUERY 5
# Top 10 Highest Salary Packages
# ==========================================

print("\n" + "=" * 60)
print("QUERY 5: Top 10 Highest Salary Packages")
print("=" * 60)

start = time.perf_counter()

query5 = (
    df.sort_values(
        "salary_package_lpa",
        ascending=False
    )
    .head(10)
)

time5 = time.perf_counter() - start

print(query5.to_string(index=False))
print("\nExecution Time:", round(time5, 4), "seconds")

query5.to_csv("pandas_query5.csv", index=False)


# ==========================================
# BENCHMARK SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("PANDAS BENCHMARK SUMMARY")
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