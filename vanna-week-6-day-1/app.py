from flask import Flask, request, jsonify
import requests
import duckdb
import re
import json


app = Flask(__name__)

# --------------------------------------------------
# Configuration
# --------------------------------------------------

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"
DB_PATH = "analytics.duckdb"


# --------------------------------------------------
# Database schema
# --------------------------------------------------

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
"""


# --------------------------------------------------
# Build prompt for Llama
# --------------------------------------------------

def build_prompt(question):

    return f"""
You are an expert DuckDB SQL analyst.

Generate ONE SQL query for the user's question.

DATABASE SCHEMA:
{SCHEMA}

Business rules:
1. Use only the table named sales.
2. Never use sales_table.
3. Use only columns from the schema.
4. Generate only a SELECT query.
5. Always include FROM sales.
6. Do not explain the answer.
7. Do not use markdown code fences.
8. Return only executable SQL.
9. If the question asks for something "by category", include category in SELECT and GROUP BY.
10. "Highest sales city" means GROUP BY city, ORDER BY SUM(sales) DESC, LIMIT 1.
11. "Lowest sales city" means GROUP BY city, ORDER BY SUM(sales) ASC, LIMIT 1.
12. "Total sales for Electronics" means WHERE category = 'Electronics'.
13. "Total sales for Furniture" means WHERE category = 'Furniture'.
14. "Total quantity sold" means SUM(quantity) FROM sales.
15. For average customer rating by category, include:
    category, AVG(customer_rating)
    and GROUP BY category.

Examples:

Question: What is the total sales?
SQL:
SELECT SUM(sales) AS total_sales FROM sales;

Question: What is the average sales?
SQL:
SELECT AVG(sales) AS average_sales FROM sales;

Question: Which city has the highest sales?
SQL:
SELECT city, SUM(sales) AS total_sales
FROM sales
GROUP BY city
ORDER BY total_sales DESC
LIMIT 1;

Question: How many products are in each category?
SQL:
SELECT category, COUNT(*) AS product_count
FROM sales
GROUP BY category
ORDER BY product_count DESC;

Question: What is the average customer rating by category?
SQL:
SELECT category, AVG(customer_rating) AS average_rating
FROM sales
GROUP BY category
ORDER BY average_rating DESC;

User question:
{question}

Return ONLY the SQL query.
"""


# --------------------------------------------------
# Extract SQL from Llama response
# --------------------------------------------------

def extract_sql(raw_response):

    text = raw_response.strip()

    print("\nLlama raw response:")
    print(text)

    # Remove markdown code fences
    text = re.sub(r"```sql", "", text, flags=re.IGNORECASE)
    text = text.replace("```", "").strip()

    # --------------------------------------------------
    # Case 1: JSON response containing "sql"
    # --------------------------------------------------

    try:
        parsed = json.loads(text)

        if isinstance(parsed, dict) and "sql" in parsed:
            text = str(parsed["sql"]).strip()

    except (json.JSONDecodeError, TypeError):
        pass

    # --------------------------------------------------
    # Case 2: Tool-style JSON containing SQL
    # Example:
    # {"name":"run_sql","parameters":{"sql":"SELECT ..."}}
    # --------------------------------------------------

    sql_match = re.search(
        r'"sql"\s*:\s*"((?:\\.|[^"\\])*)"',
        text,
        flags=re.IGNORECASE | re.DOTALL
    )

    if sql_match:
        try:
            extracted = json.loads(f'"{sql_match.group(1)}"')
            text = extracted.strip()
        except json.JSONDecodeError:
            text = sql_match.group(1).replace('\\"', '"').strip()

    # --------------------------------------------------
    # Find SELECT statement
    # --------------------------------------------------

    match = re.search(
        r"\bSELECT\b.*",
        text,
        flags=re.IGNORECASE | re.DOTALL
    )

    if not match:
        raise ValueError(
            f"No SELECT statement found in model response: {raw_response}"
        )

    sql = match.group(0).strip()

    # Remove anything after the first semicolon
    if ";" in sql:
        sql = sql.split(";", 1)[0].strip() + ";"

    return sql


# --------------------------------------------------
# Generate SQL using Ollama
# --------------------------------------------------

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

    raw_response = response.json().get("response", "").strip()

    if not raw_response:
        raise ValueError("Ollama returned an empty response.")

    return extract_sql(raw_response)


# --------------------------------------------------
# Validate SQL
# --------------------------------------------------

def validate_sql(sql):

    sql_lower = sql.lower().strip()

    # Must be SELECT
    if not sql_lower.startswith("select"):
        raise ValueError("Only SELECT queries are allowed.")

    # Prevent invalid table
    if "sales_table" in sql_lower:
        raise ValueError("Invalid table name: sales_table.")

    # Prevent dangerous statements
    forbidden_keywords = [
        "drop ",
        "delete ",
        "update ",
        "insert ",
        "alter ",
        "truncate ",
        "create ",
        "replace ",
        "attach ",
        "detach "
    ]

    for keyword in forbidden_keywords:
        if keyword in sql_lower:
            raise ValueError(
                f"SQL operation is not allowed: {keyword.strip().upper()}"
            )

    # Must query sales table
    if not re.search(r"\bfrom\s+sales\b", sql_lower):
        raise ValueError("Query must use the sales table.")

    return True


# --------------------------------------------------
# Execute SQL in DuckDB
# --------------------------------------------------

def execute_sql(sql):

    connection = duckdb.connect(DB_PATH)

    try:
        result = connection.execute(sql).fetchdf()

        return result.to_dict(orient="records")

    finally:
        connection.close()


# --------------------------------------------------
# CIA SQL Analyst Endpoint
# --------------------------------------------------

@app.route("/cia/sql-analyst", methods=["POST"])
def sql_analyst():

    try:

        # Get JSON body
        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "success": False,
                "error": "Request body is required."
            }), 400

        # Get question
        question = data.get("question")

        if not question or not isinstance(question, str):
            return jsonify({
                "success": False,
                "error": "question is required and must be a string."
            }), 400

        question = question.strip()

        if not question:
            return jsonify({
                "success": False,
                "error": "question cannot be empty."
            }), 400

        print("\n" + "=" * 70)
        print("CIA SQL ANALYST REQUEST")
        print("=" * 70)
        print("Question:", question)

        # Generate SQL
        sql = generate_sql(question)

        print("\nGenerated SQL:")
        print(sql)

        # Validate SQL
        validate_sql(sql)

        print("SQL validation: PASSED")

        # Execute SQL
        result = execute_sql(sql)

        print("\nDatabase result:")
        print(result)

        return jsonify({
            "success": True,
            "question": question,
            "sql": sql,
            "result": result
        }), 200

    except requests.exceptions.RequestException as error:

        return jsonify({
            "success": False,
            "error": f"Ollama connection error: {str(error)}"
        }), 500

    except Exception as error:

        print("\nERROR:")
        print(str(error))

        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


# --------------------------------------------------
# Start Flask
# --------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False
    )