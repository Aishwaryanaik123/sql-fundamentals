import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

queries = [
    ("1. Count sales", "SELECT COUNT(*) FROM sales;"),
    ("2. Total sales amount", "SELECT SUM(quantity * price) FROM sales;"),
    ("3. Average product price", "SELECT AVG(price) FROM sales;"),
    ("4. Region with most sales", "SELECT region, COUNT(*) FROM sales GROUP BY region ORDER BY COUNT(*) DESC;"),
    ("5. Total quantity sold", "SELECT SUM(quantity) FROM sales;"),
    ("6. Laptops sold", "SELECT SUM(quantity) FROM sales WHERE product = 'Laptop';"),
    ("7. Highest product price", "SELECT MAX(price) FROM sales;"),
    ("8. Bangalore sales", "SELECT COUNT(*) FROM sales WHERE region = 'Bangalore';"),
    ("9. Phones quantity", "SELECT SUM(quantity) FROM sales WHERE product = 'Phone';"),
    ("10. Average laptop price", "SELECT AVG(price) FROM sales WHERE product = 'Laptop';")
]

for name, sql in queries:
    cursor.execute(sql)
    result = cursor.fetchall()
    print(f"{name}: {result}")

conn.close()