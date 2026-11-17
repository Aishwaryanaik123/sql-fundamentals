-- Week 12 Day 2: five analytical SQL queries
-- Run with src/run_analysis.py

-- Q1: Overall business KPIs
SELECT COUNT(*) AS order_lines, ROUND(SUM(sales), 2) AS total_sales,
       ROUND(SUM(profit), 2) AS total_profit, ROUND(AVG(sales), 2) AS avg_line_sales
FROM sales;

-- Q2: Sales and profit by region
SELECT region, ROUND(SUM(sales), 2) AS total_sales, ROUND(SUM(profit), 2) AS total_profit
FROM sales GROUP BY region ORDER BY total_sales DESC;

-- Q3: Category performance
SELECT category, COUNT(*) AS order_lines, ROUND(SUM(sales), 2) AS total_sales,
       ROUND(SUM(profit), 2) AS total_profit
FROM sales GROUP BY category ORDER BY total_sales DESC;

-- Q4: Monthly sales trend
SELECT DATE_TRUNC('month', CAST(order_date AS DATE)) AS sales_month,
       ROUND(SUM(sales), 2) AS monthly_sales
FROM sales GROUP BY 1 ORDER BY 1;

-- Q5: Customer segment performance
SELECT customer_segment, COUNT(*) AS order_lines, ROUND(SUM(sales), 2) AS total_sales,
       ROUND(AVG(discount_pct) * 100, 2) AS avg_discount_percent
FROM sales GROUP BY customer_segment ORDER BY total_sales DESC;
