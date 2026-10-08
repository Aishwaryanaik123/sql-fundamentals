import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "sales.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

cursor.execute("SELECT * FROM sales;")
for row in cursor.fetchall():
    print(row)

conn.close()
