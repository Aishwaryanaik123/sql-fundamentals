-- Superset chart SQL; table name: sales_performance
-- KPI metrics
SELECT SUM(sales) AS total_sales, SUM(profit) AS total_profit,
       SUM(orders) AS total_orders, SUM(sales)/NULLIF(SUM(orders),0) AS average_order_value
FROM sales_performance;

-- Bar: sales by region
SELECT region, SUM(sales) AS total_sales FROM sales_performance GROUP BY region ORDER BY total_sales DESC;

-- Line: monthly sales trend
SELECT DATE_TRUNC('month', CAST(order_date AS DATE)) AS month, SUM(sales) AS total_sales
FROM sales_performance GROUP BY 1 ORDER BY 1;

-- Pie: product category mix
SELECT product_category, SUM(sales) AS total_sales FROM sales_performance GROUP BY product_category;

-- Table: regional summary
SELECT region, SUM(orders) AS total_orders, SUM(sales) AS total_sales,
       SUM(profit) AS total_profit, SUM(profit)/NULLIF(SUM(sales),0) AS profit_margin
FROM sales_performance GROUP BY region ORDER BY total_sales DESC;
