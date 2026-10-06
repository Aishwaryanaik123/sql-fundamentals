from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.post("/cia/sql-analyst")
def sql_analyst(question: str):

    queries = {
        "How many sales records are there?":
            "SELECT COUNT(*) AS total_sales FROM sales;",

        "What is the total sales amount?":
            "SELECT SUM(quantity * price) AS total_sales_amount FROM sales;",

        "What is the average product price?":
            "SELECT AVG(price) AS average_price FROM sales;",

        "Which region has the most sales records?":
            """SELECT region, COUNT(*) AS sales_count
               FROM sales
               GROUP BY region
               ORDER BY sales_count DESC;""",

        "What is the total quantity sold?":
            "SELECT SUM(quantity) AS total_quantity FROM sales;"
    }

    if question not in queries:
        return {
            "error": "Question not found in training examples"
        }

    sql = queries[question]

    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    cursor.execute(sql)
    result = cursor.fetchall()

    conn.close()

    return {
        "question": question,
        "sql": sql,
        "result": result
    }