-- Week 11 Day 5: Stakeholder Report — 5 Business Insights
-- Load sales_performance_2024_2025.csv into a table named sales_performance.

-- 1. Annual sales growth
SELECT year, SUM(sales) AS total_sales
FROM sales_performance GROUP BY year ORDER BY year;

-- 2. Regional sales contribution and profit margin
SELECT region, SUM(sales) AS sales,
       100.0 * SUM(sales) / (SELECT SUM(sales) FROM sales_performance) AS sales_share_pct,
       100.0 * SUM(profit) / SUM(sales) AS profit_margin_pct
FROM sales_performance GROUP BY region ORDER BY sales DESC;

-- 3. Product category mix
SELECT product_category, SUM(sales) AS sales,
       100.0 * SUM(sales) / (SELECT SUM(sales) FROM sales_performance) AS sales_share_pct
FROM sales_performance GROUP BY product_category ORDER BY sales DESC;

-- 4. Monthly trend and Q4 seasonality
SELECT month, SUM(sales) AS monthly_sales
FROM sales_performance GROUP BY month ORDER BY month;

-- 5. Regional profitability comparison
SELECT region, SUM(profit) / SUM(sales) * 100.0 AS profit_margin_pct
FROM sales_performance GROUP BY region ORDER BY profit_margin_pct;
