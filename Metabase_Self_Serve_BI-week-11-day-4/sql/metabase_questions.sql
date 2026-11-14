-- Metabase saved-question SQL reference
-- Table: public.sales_performance

-- 1. Metric: Total Sales
SELECT SUM(sales) AS total_sales FROM sales_performance;

-- 2. Metric: Total Profit
SELECT SUM(profit) AS total_profit FROM sales_performance;

-- 3. Metric: Total Orders
SELECT SUM(orders) AS total_orders FROM sales_performance;

-- 4. Metric: Average Order Value
SELECT SUM(sales) / NULLIF(SUM(orders), 0) AS average_order_value
FROM sales_performance;

-- 5. Bar chart: Sales by Region
SELECT region, SUM(sales) AS total_sales
FROM sales_performance
GROUP BY region
ORDER BY total_sales DESC;

-- 6. Line chart: Monthly Sales Trend
SELECT CAST(order_date AS DATE) AS month, SUM(sales) AS total_sales
FROM sales_performance
GROUP BY CAST(order_date AS DATE)
ORDER BY month;

-- 7. Pie chart: Sales Mix by Product Category
SELECT product_category, SUM(sales) AS total_sales
FROM sales_performance
GROUP BY product_category
ORDER BY total_sales DESC;

-- 8. Table: Regional Summary
SELECT region, SUM(orders) AS total_orders, SUM(sales) AS total_sales,
       SUM(profit) AS total_profit,
       SUM(profit) / NULLIF(SUM(sales), 0) AS profit_margin
FROM sales_performance
GROUP BY region
ORDER BY total_sales DESC;
