\# Automated EDA - Week 5 Day 3



\## Objective



The objective of this task is to load a 100,000-row CSV dataset into

DuckDB, perform analytical SQL queries, benchmark DuckDB against

Pandas, and perform the same operations using Polars.



\## Dataset



File: `student\_performance.csv`



Rows: 100,000



Columns: 18



\## Columns



\- branch

\- college\_tier

\- cgpa

\- backlogs

\- coding\_skills

\- dsa\_score

\- aptitude\_score

\- communication\_skills

\- ml\_knowledge

\- system\_design

\- internships

\- projects\_count

\- certifications

\- hackathons

\- open\_source\_contributions

\- extracurriculars

\- placement\_status

\- salary\_package\_lpa



\## Tasks Completed



1\. Loaded the 100,000-row CSV dataset.

2\. Loaded the dataset into DuckDB.

3\. Executed 5 analytical SQL queries.

4\. Benchmarked DuckDB against Pandas.

5\. Loaded the same dataset into Polars.

6\. Performed the same analytical operations using Polars.

7\. Compared Pandas, DuckDB, and Polars.

8\. Documented syntax and performance differences.



\## DuckDB Analytical Queries



\### 1. Count Total Rows



Result: 100,000



\### 2. Average CGPA



Result: 7.206381



\### 3. Average Salary by Branch



| Branch | Average Salary |

|---|---:|

| CE | 17.348112 |

| CSE | 17.326434 |

| Chemical | 17.311982 |

| EE | 17.303424 |

| ME | 17.301258 |

| ECE | 17.291240 |

| IT | 17.277354 |



\### 4. Placement Status



| Placement Status | Student Count |

|---:|---:|

| 0 | 31,525 |

| 1 | 68,475 |



\### 5. Average Salary by College Tier



| College Tier | Average Salary |

|---|---:|

| Tier-1 | 19.341536 |

| Tier-2 | 17.169251 |

| Tier-3 | 16.531575 |



\## Benchmark Results



| Operation | Pandas | DuckDB | Polars |

|---|---:|---:|---:|

| Count Rows | 0.000008 s | 0.010756 s | 0.000004 s |

| Average CGPA | 0.000492 s | 0.009042 s | 0.002443 s |

| Salary by Branch | 0.010812 s | 0.016874 s | 0.006859 s |

| Placement Status | 0.001658 s | 0.024351 s | 0.001870 s |

| Salary by College Tier | 0.010797 s | 0.016855 s | 0.002169 s |



\## Tools Used



\- Python 3.11.9

\- Pandas 3.0.6

\- DuckDB 1.5.6

\- Polars 1.44.2

\- VS Code

\- PowerShell

\- Git

\- GitHub



\## Conclusion



Pandas is convenient for general Python-based data analysis.

DuckDB provides SQL-based analytical querying, while Polars provides

a high-performance DataFrame approach.



The benchmark results are based on a single execution and may vary

depending on the computer, Python environment, system load, and

number of benchmark repetitions.

