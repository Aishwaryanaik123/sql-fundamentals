SHOW DATABASES;

USE sql_practice_db;

SHOW TABLES;

-- 1. INNER JOIN
SELECT c.CustomerID, c.CustomerName, o.OrderID
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID;

DESCRIBE customers;

DESCRIBE orders;

DESCRIBE order_details;

DESCRIBE employees;

USE sql_practice_db;

-- 1. INNER JOIN
SELECT 
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date,
    o.order_status
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id;
    
-- 2. LEFT JOIN
SELECT 
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date,
    o.order_status
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id;
    
-- 3. RIGHT JOIN
SELECT 
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date,
    o.order_status
FROM customers c
RIGHT JOIN orders o
    ON c.customer_id = o.customer_id;
    

-- 4. FULL OUTER JOIN
-- MySQL does not directly support FULL OUTER JOIN
SELECT 
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date,
    o.order_status
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id  
    
UNION

SELECT 
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date,
    o.order_status
FROM customers c
RIGHT JOIN orders o
    ON c.customer_id = o.customer_id;    
    
-- 5. FIND CUSTOMERS WITH MULTIPLE ORDERS
SELECT 
    customer_id,
    COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- 6. SELF JOIN
SELECT 
    e.employee_id,
    e.employee_name AS employee,
    m.employee_name AS manager
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.employee_id;
    