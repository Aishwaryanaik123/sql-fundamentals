import requests
import duckdb

from train_vanna import training_examples


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"
DB_PATH = "analytics.duckdb"


SCHEMA = """
Database: analytics.duckdb

Table:
sales

Columns:
id INTEGER
product VARCHAR
category VARCHAR
city VARCHAR
sales DOUBLE
quantity INTEGER
customer_rating DOUBLE

Important:
The table name is exactly "sales".
There is no table named "sales_table".
"""


def build_prompt(question):
    examples = ""

    for example in training_examples:
        examples += f"""
Question:
{example.question}

SQL:
{example.args["sql"].strip()}

"""

    return f"""
You are a DuckDB SQL expert.

Generate SQL for the user's question.

DATABASE SCHEMA:
{SCHEMA}

Here are five examples showing the correct question-to-SQL pattern:
{examples}

Rules:
1. Use only the table and columns provided in the schema.
2. The table name is exactly sales.
3. Never use sales_table.
4. Generate only a SELECT SQL query.
5. Do not explain the answer.
6. Do not use markdown code fences.
7. Return only executable DuckDB SQL.

User question:
{question}
"""


def generate_sql(question):

    prompt = build_prompt(question)

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0
            }
        },
        timeout=120
    )

    response.raise_for_status()

    sql = response.json()["response"].strip()

    # Remove markdown code fences if the model adds them
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql


def validate_sql(sql):

    sql_lower = sql.lower().strip()

    if not sql_lower.startswith("select"):
        raise ValueError("Only SELECT queries are allowed.")

    if "sales_table" in sql_lower:
        raise ValueError("Invalid table name sales_table.")

    if " sales " not in f" {sql_lower} " and "from sales" not in sql_lower:
        raise ValueError("Query does not appear to use the sales table.")

    return True


def execute_sql(sql):

    connection = duckdb.connect(DB_PATH)

    try:
        result = connection.execute(sql).fetchdf()
        return result
    finally:
        connection.close()


def main():

    question = "What is the total sales?"

    print("=" * 70)
    print("QUESTION")
    print("=" * 70)
    print(question)

    print("\nGenerating SQL...\n")

    sql = generate_sql(question)

    print("=" * 70)
    print("GENERATED SQL")
    print("=" * 70)
    print(sql)

    print("\nValidating SQL...")

    validate_sql(sql)

    print("SQL validation: PASSED")

    print("\nExecuting SQL in DuckDB...\n")

    result = execute_sql(sql)

    print("=" * 70)
    print("RESULT")
    print("=" * 70)
    print(result)


if __name__ == "__main__":
    main()