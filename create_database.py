import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    customer_name TEXT,
    product TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL,
    region TEXT
)
""")

# Sample data
sales_data = [
    (1, "Rahul", "Laptop", "Electronics", 2, 60000, "Bangalore"),
    (2, "Priya", "Phone", "Electronics", 5, 25000, "Mumbai"),
    (3, "Arun", "Chair", "Furniture", 10, 5000, "Bangalore"),
    (4, "Sneha", "Laptop", "Electronics", 1, 65000, "Delhi"),
    (5, "Kiran", "Table", "Furniture", 4, 8000, "Mumbai"),
    (6, "Anita", "Phone", "Electronics", 3, 22000, "Bangalore"),
    (7, "Vijay", "Chair", "Furniture", 6, 4500, "Delhi"),
    (8, "Meena", "Laptop", "Electronics", 2, 62000, "Mumbai")
]

# Insert data
cursor.executemany("""
INSERT OR IGNORE INTO sales
(id, customer_name, product, category, quantity, price, region)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", sales_data)

conn.commit()

# Display records
cursor.execute("SELECT * FROM sales")
rows = cursor.fetchall()

print("Database created successfully!")
print(f"Total records: {len(rows)}")
print("\nSales Data:")

for row in rows:
    print(row)

conn.close()