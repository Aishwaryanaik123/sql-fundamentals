-- Example SQL queries used for the dashboard
-- Connect student_placement.db / table: student_placement

-- 1. Average salary by branch
SELECT branch, ROUND(AVG(salary_package_lpa), 2) AS avg_salary_lpa
FROM student_placement
GROUP BY branch
ORDER BY avg_salary_lpa DESC;

-- 2. Monthly salary trend
SELECT month, ROUND(AVG(salary_package_lpa), 2) AS avg_salary_lpa
FROM student_placement
GROUP BY month
ORDER BY month;

-- 3. Placement distribution
SELECT placement_status, COUNT(*) AS students
FROM student_placement
GROUP BY placement_status;

-- 4. Overall placement metric
SELECT ROUND(
    100.0 * SUM(CASE WHEN placement_status = 'Placed' THEN 1 ELSE 0 END) / COUNT(*), 2
) AS placement_rate
FROM student_placement;

-- 5. College tier summary
SELECT college_tier,
       COUNT(*) AS students,
       ROUND(100.0 * SUM(CASE WHEN placement_status='Placed' THEN 1 ELSE 0 END) / COUNT(*), 1) AS placement_rate,
       ROUND(AVG(salary_package_lpa), 2) AS avg_salary_lpa,
       ROUND(AVG(cgpa), 2) AS avg_cgpa
FROM student_placement
GROUP BY college_tier
ORDER BY college_tier;
