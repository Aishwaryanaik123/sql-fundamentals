# Three Initial Insights

Dataset reference: `student_performance.csv` (100,000 rows and 18 columns, based on the previously recorded dataset summary).

1. **Placement status is not evenly split.** The recorded counts are 68,475 placed and 31,525 not placed, so approximately 68.5% of records are marked placed. Confirm the meaning of the placement-status field before using this as a placement-rate KPI.
2. **Salary data has substantial missingness.** `salary_package_lpa` has 31,525 missing values. Salary averages may be biased if missingness is related to placement status or another group; report the denominator and missing-data treatment.
3. **Average salary differs only modestly across branches in the saved summary.** The recorded branch averages are close to one another (roughly 17.28–17.35 LPA). Validate sample sizes and statistical uncertainty before interpreting these small differences as meaningful.
