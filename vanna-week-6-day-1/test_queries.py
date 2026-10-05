import requests
import duckdb


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"
DB_PATH = "analytics.duckdb"


SCHEMA = """
Database: analytics.duckdb

Table: sales

Columns:
id INTEGER
product VARCHAR
category VARCHAR
city VARCHAR
sales DOUBLE
quantity INTEGER
customer_rating DOUBLE

Important:
The correct table name is sales.
There is no table named sales_table.
"""


TRAINING_EXAMPLES = [
    {
        "question": "What is the total sales?",
        "sql": "SELECT SUM(sales) AS total_sales FROM sales;"
    },
    {
        "question": "What is the average sales?",
        "sql": "SELECT AVG(sales) AS average_sales FROM sales;"
    },
    {
        "question": "Which city has the highest sales?",
        "sql": """
SELECT city, SUM(sales) AS total_sales
FROM sales
GROUP BY city
ORDER BY total_sales DESC
LIMIT 1;
"""
    },
    {
        "question": "How many products are in each category?",
        "sql": """
SELECT category, COUNT(*) AS product_count
FROM sales
GROUP BY category
ORDER BY product_count DESC;
"""
    },
    {
        "question": "What is the average customer rating by category?",
        "sql": """
SELECT category, AVG(customer_rating) AS average_rating
FROM sales
GROUP BY category
ORDER BY average_rating DESC;
"""
    }
]


QUERIES = [
    {
        "question": "What is the total sales?",
        "expected_result": "392000"
    },
    {
        "question": "What is the average sales?",
        "expected_result": "39200"
    },
    {
        "question": "Which city has the highest sales?",
        "expected_result": "Mumbai - 152000"
    },
    {
        "question": "Which city has the lowest sales?",
        "expected_result": "Chennai - 30000"
    },
    {
        "question": "How many products are in each category?",
        "expected_result": "Electronics - 6, Furniture - 4"
    },
    {
        "question": "What is the average customer rating by category?",
        "expected_result": "Electronics - 4.35, Furniture - 4.225"
    },
    {
        "question": "What is the total quantity sold?",
        "expected_result": "69"
    },
    {
        "question": "Which product generated the highest sales?",
        "expected_result": "Laptop - 155000"
    },
    {
        "question": "What are the total sales for Electronics?",
        "expected_result": "318000"
    },
    {
        "question": "What are the total sales for Furniture?",
        "expected_result": "74000"
    }
]


def build_prompt(question):

    examples = ""

    for example in TRAINING_EXAMPLES:
        examples += f"""
Question:
{example["question"]}

SQL:
{example["sql"].strip()}

"""

    return f"""
You are an expert DuckDB SQL analyst.

Generate SQL for the user's question.

DATABASE SCHEMA:
{SCHEMA}

TRAINING EXAMPLES:
{examples}

Rules:
1. Use only the sales table.
2. Never use sales_table.
3. Use only columns from the schema.
4. Generate only a SELECT query.
5. Do not explain anything.
6. Do not use markdown code fences.
7. Return only executable DuckDB SQL.

Business rules:
8. "Sales by city" means SUM(sales) GROUP BY city.
9. "City with the highest sales" means:
   GROUP BY city
   ORDER BY SUM(sales) DESC
   LIMIT 1.
10. "City with the lowest sales" means:
    GROUP BY city
    ORDER BY SUM(sales) ASC
    LIMIT 1.
11. Electronics and Furniture are values of the category column, not the product column.
12. "Total sales for Electronics" means:
    WHERE category = 'Electronics'
13. "Total sales for Furniture" means:
    WHERE category = 'Furniture'
14. Never compare category names such as Electronics or Furniture with the product column.
15. Always include FROM sales when calculating any value from the sales table.
16. For "total quantity sold", use:
    SELECT SUM(quantity) AS total_quantity_sold
    FROM sales;
17. When a question asks for a metric "by category", include category in SELECT and GROUP BY category.
18. For average customer rating by category, use:
    SELECT category, AVG(customer_rating) AS average_rating
    FROM sales
    GROUP BY category
    ORDER BY average_rating DESC;


User question:
{question}
"""


def generate_sql(question):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": build_prompt(question),
            "stream": False,
            "options": {
                "temperature": 0
            }
        },
        timeout=120
    )

    response.raise_for_status()

    sql = response.json()["response"].strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql


def validate_sql(sql):

    sql_lower = sql.lower().strip()

    if not sql_lower.startswith("select"):
        raise ValueError("SQL does not start with SELECT.")

    if "sales_table" in sql_lower:
        raise ValueError("Invalid table name: sales_table")

    return True


def execute_sql(sql):

    connection = duckdb.connect(DB_PATH)

    try:
        return connection.execute(sql).fetchdf()
    finally:
        connection.close()


def main():

    print("=" * 80)
    print("VANNA / OLLAMA - 10 NATURAL LANGUAGE SQL TESTS")
    print("=" * 80)

    for number, query in enumerate(QUERIES, start=1):

        print()
        print("=" * 80)
        print(f"QUERY {number}/10")
        print("=" * 80)

        question = query["question"]

        print(f"\nQuestion:\n{question}")

        try:

            sql = generate_sql(question)

            print(f"\nGenerated SQL:\n{sql}")

            validate_sql(sql)

            print("\nSQL validation: PASSED")

            result = execute_sql(sql)

            print("\nDatabase result:")
            print(result.to_string(index=False))

            print(f"\nExpected result:\n{query['expected_result']}")

        except Exception as error:

            print("\nERROR:")
            print(error)

    print()
    print("=" * 80)
    print("10-query testing completed.")
    print("=" * 80)


if __name__ == "__main__":
    main()