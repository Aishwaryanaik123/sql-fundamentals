use sales ;

-- 1. non-correlated subquery - above average sales
SELECT *
FROM sales
WHERE amount > (
    SELECT AVG(amount)
    FROM sales
);

-- 2. correlated subquery - top performer per region
SELECT s.*
FROM sales s
WHERE amount = (
    SELECT MAX(s2.amount)
    FROM sales s2
    WHERE s2.region = s.region
);


-- 3. rewrite a nested subquery as a CTE
-- using a nested subquery
SELECT *
FROM (
    SELECT region, SUM(amount) AS total_sales
    FROM sales
    GROUP BY region
) AS regional_sales
WHERE total_sales > 20000;


-- using a CTE
WITH regional_sales AS (
    SELECT region, SUM(amount) AS total_sales
    FROM sales
    GROUP BY region
)
SELECT *
FROM regional_sales
WHERE total_sales > 20000;


--  4. chain 2 CTEs in a single query
WITH regional_sales AS (
    SELECT region, SUM(amount) AS total_sales
    FROM sales
    GROUP BY region
),
high_sales_regions AS (
    SELECT region, total_sales
    FROM regional_sales
    WHERE total_sales > 20000
)
SELECT *
FROM high_sales_regions;