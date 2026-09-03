CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    region VARCHAR(50),
    category VARCHAR(50),
    order_date DATE,
    amount DECIMAL(10,2)
);

INSERT INTO sales VALUES
(1, 'North', 'Electronics', '2026-01-10', 50000),
(2, 'South', 'Furniture', '2026-01-15', 25000),
(3, 'North', 'Electronics', '2026-02-05', 30000),
(4, 'East', 'Clothing', '2026-02-20', 15000),
(5, 'South', 'Electronics', '2026-03-12', 40000),
(6, 'West', 'Furniture', '2026-03-25', 20000),
(7, 'East', 'Clothing', '2026-04-08', 18000),
(8, 'West', 'Electronics', '2026-04-18', 35000);

SELECT * FROM sales;

-- 1. Count total sales
SELECT COUNT(*) AS total_sales
FROM sales;

-- 2. Count sales by region
SELECT region, COUNT(*) AS total_sales
FROM sales
GROUP BY region;

-- 3. Calculate total sales amount
SELECT SUM(amount) AS total_amount
FROM sales;

-- 4. Calculate total sales by category
SELECT category, SUM(amount) AS total_amount
FROM sales
GROUP BY category;

-- 5. Calculate average sales amount
SELECT AVG(amount) AS average_amount
FROM sales;

-- 6. Calculate average sales by region
SELECT region, AVG(amount) AS average_amount
FROM sales
GROUP BY region;

-- 7. Find highest sale
SELECT MAX(amount) AS highest_sale
FROM sales;

-- 8. Find lowest sale
SELECT MIN(amount) AS lowest_sale
FROM sales;

-- 9. Group sales by region
SELECT region, SUM(amount) AS total_sales
FROM sales
GROUP BY region;

-- 10. Group sales by category
SELECT category, SUM(amount) AS total_sales
FROM sales
GROUP BY category;

-- 11. Group sales by month
SELECT MONTH(order_date) AS sales_month, SUM(amount) AS total_sales
FROM sales
GROUP BY MONTH(order_date)
ORDER BY sales_month;

-- 12. Regions with total sales greater than 50000
SELECT region, SUM(amount) AS total_sales
FROM sales
GROUP BY region
HAVING SUM(amount) > 50000;

-- 13. Running total of sales
SELECT
    sale_id,
    order_date,
    amount,
    SUM(amount) OVER (ORDER BY order_date) AS running_total
FROM sales;