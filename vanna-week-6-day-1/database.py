import duckdb

DB_PATH = "analytics.duckdb"

connection = duckdb.connect(DB_PATH)

connection.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER,
    product VARCHAR,
    category VARCHAR,
    city VARCHAR,
    sales DOUBLE,
    quantity INTEGER,
    customer_rating DOUBLE
)
""")

connection.execute("DELETE FROM sales")

connection.execute("""
INSERT INTO sales VALUES
(1, 'Laptop', 'Electronics', 'Bangalore', 75000, 5, 4.5),
(2, 'Phone', 'Electronics', 'Mumbai', 50000, 10, 4.2),
(3, 'Chair', 'Furniture', 'Bangalore', 12000, 8, 4.0),
(4, 'Desk', 'Furniture', 'Delhi', 25000, 4, 4.3),
(5, 'Tablet', 'Electronics', 'Chennai', 30000, 7, 4.1),
(6, 'Laptop', 'Electronics', 'Mumbai', 80000, 3, 4.7),
(7, 'Chair', 'Furniture', 'Delhi', 15000, 6, 4.4),
(8, 'Phone', 'Electronics', 'Bangalore', 55000, 12, 4.6),
(9, 'Desk', 'Furniture', 'Mumbai', 22000, 5, 4.2),
(10, 'Tablet', 'Electronics', 'Delhi', 28000, 9, 4.0)
""")

print("Database created successfully.")
print("Table: sales")
print("Rows:", connection.execute("SELECT COUNT(*) FROM sales").fetchone()[0])

connection.close()