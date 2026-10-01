import duckdb
import time

# ==========================================
# 1. CONNECT TO DUCKDB
# ==========================================

con = duckdb.connect()

csv_file = "student_performance.csv"

print("=" * 60)
print("DUCKDB ANALYSIS")
print("=" * 60)


# ==========================================
# 2. CHECK DATASET
# ==========================================

start = time.perf_counter()

row_count = con.execute(f"""
    SELECT COUNT(*)
    FROM read_csv_auto('{csv_file}')
""").fetchone()[0]

load_time = time.perf_counter() - start

print("\nDataset Information")
print("-" * 60)
print("CSV File:", csv_file)
print("Total Rows:", row_count)
print("Time:", round(load_time, 4), "seconds")


# ==========================================
# 3. SHOW COLUMN NAMES
# ==========================================

columns = con.execute(f"""
    DESCRIBE SELECT *
    FROM read_csv_auto('{csv_file}')
""").fetchdf()

print("\nColumns:")
print(columns[["column_name", "column_type"]].to_string(index=False))


# ==========================================
# QUERY 1
# Average salary by branch
# ==========================================

print("\n" + "=" * 60)
print("QUERY 1: Average Salary by Branch")
print("=" * 60)

start = time.perf_counter()

query1 = con.execute(f"""
    SELECT
        branch,
        ROUND(AVG(salary_package_lpa), 2) AS avg_salary
    FROM read_csv_auto('{csv_file}')
    GROUP BY branch
    ORDER BY avg_salary DESC
""").fetchdf()

time1 = time.perf_counter() - start

print(query1)
print("\nExecution Time:", round(time1, 4), "seconds")

query1.to_csv("duckdb_query1.csv", index=False)


# ==========================================
# QUERY 2
# Average CGPA by college tier
# ==========================================

print("\n" + "=" * 60)
print("QUERY 2: Average CGPA by College Tier")
print("=" * 60)

start = time.perf_counter()

query2 = con.execute(f"""
    SELECT
        college_tier,
        ROUND(AVG(cgpa), 2) AS avg_cgpa
    FROM read_csv_auto('{csv_file}')
    GROUP BY college_tier
    ORDER BY avg_cgpa DESC
""").fetchdf()

time2 = time.perf_counter() - start

print(query2)
print("\nExecution Time:", round(time2, 4), "seconds")

query2.to_csv("duckdb_query2.csv", index=False)


# ==========================================
# QUERY 3
# Placement Status Count
# ==========================================

print("\n" + "=" * 60)
print("QUERY 3: Placement Status Count")
print("=" * 60)

start = time.perf_counter()

query3 = con.execute(f"""
    SELECT
        placement_status,
        COUNT(*) AS total_students
    FROM read_csv_auto('{csv_file}')
    GROUP BY placement_status
    ORDER BY total_students DESC
""").fetchdf()

time3 = time.perf_counter() - start

print(query3)
print("\nExecution Time:", round(time3, 4), "seconds")

query3.to_csv("duckdb_query3.csv", index=False)


# ==========================================
# QUERY 4
# Average Coding Skills by Branch
# ==========================================

print("\n" + "=" * 60)
print("QUERY 4: Average Coding Skills by Branch")
print("=" * 60)

start = time.perf_counter()

query4 = con.execute(f"""
    SELECT
        branch,
        ROUND(AVG(coding_skills), 2) AS avg_coding_skills
    FROM read_csv_auto('{csv_file}')
    GROUP BY branch
    ORDER BY avg_coding_skills DESC
""").fetchdf()

time4 = time.perf_counter() - start

print(query4)
print("\nExecution Time:", round(time4, 4), "seconds")

query4.to_csv("duckdb_query4.csv", index=False)


# ==========================================
# QUERY 5
# Top 10 Highest Salary Packages
# ==========================================

print("\n" + "=" * 60)
print("QUERY 5: Top 10 Highest Salary Packages")
print("=" * 60)

start = time.perf_counter()

query5 = con.execute(f"""
    SELECT *
    FROM read_csv_auto('{csv_file}')
    ORDER BY salary_package_lpa DESC
    LIMIT 10
""").fetchdf()

time5 = time.perf_counter() - start

print(query5.to_string(index=False))
print("\nExecution Time:", round(time5, 4), "seconds")

query5.to_csv("duckdb_query5.csv", index=False)


# ==========================================
# 6. BENCHMARK SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("DUCKDB BENCHMARK SUMMARY")
print("=" * 60)

print(f"Query 1 - Average salary by branch:       {time1:.4f} seconds")
print(f"Query 2 - Average CGPA by college tier:   {time2:.4f} seconds")
print(f"Query 3 - Placement status count:         {time3:.4f} seconds")
print(f"Query 4 - Coding skills by branch:        {time4:.4f} seconds")
print(f"Query 5 - Top 10 salary packages:         {time5:.4f} seconds")

total_time = time1 + time2 + time3 + time4 + time5

print("-" * 60)
print(f"Total query execution time:               {total_time:.4f} seconds")


# ==========================================
# 7. CLOSE DUCKDB
# ==========================================

con.close()

print("\nAnalysis completed successfully!")