SHOW DATABASES;

USE sql_practice_db;

SHOW TABLES;

DESCRIBE orders;

-- Query 1: Basic SELECT
SELECT *
FROM orders;

-- Query 2: SELECT specific columns
SELECT order_id, customer_id, order_date, order_status
FROM orders;

-- Query 3: WHERE with comparison operator
SELECT *
FROM orders
WHERE order_id > 400;

-- Query 4: WHERE with AND
SELECT *
FROM orders
WHERE order_id > 400
AND order_status = 'Delivered';

-- Query 5: WHERE with OR
SELECT *
FROM orders
WHERE order_status = 'Pending'
OR order_status = 'Cancelled';

-- Query 6: WHERE with NOT
SELECT *
FROM orders
WHERE NOT order_status = 'Cancelled';

DESCRIBE customers;

-- Query 7: LIKE
SELECT *
FROM customers
WHERE customer_name LIKE 'A%';

SELECT DISTINCT city
FROM customers;

-- Query 8: IN
SELECT *
FROM customers
WHERE city IN ('Bangalore', 'Mumbai', 'Hyderabad');

-- Query 9: BETWEEN
SELECT *
FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31';

-- Query 10: IS NULL (1)
SELECT *
FROM customers
WHERE phone IS NULL;

-- (2)
SELECT *
FROM customers
WHERE city IS NULL;

-- (3)
SELECT *
FROM customers
WHERE customer_status IS NULL;
