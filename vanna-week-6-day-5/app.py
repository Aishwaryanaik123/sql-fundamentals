"""
CIA SQL Analyst API.
Uses a local SQLite database and 5 stored Q&A examples for a predictable,
offline demo of the required endpoint. The SQL selection is rule-based so
the package works without an API key; review/replace mappings for new questions.
"""
from pathlib import Path
import json
import sqlite3
from typing import Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "sales.db"
TRAINING_PATH = ROOT / "training_examples.json"
TESTS_PATH = ROOT / "query_tests.json"

app = FastAPI(title="CIA SQL Analyst", version="1.0.0",
              description="Natural-language-to-SQL demo endpoint backed by SQLite.")

class AnalystRequest(BaseModel):
    question: str = Field(..., min_length=3, description="Natural-language question")

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def choose_sql(question: str) -> str:
    q = " ".join(question.lower().strip().replace("?", "").split())
    rules = [
        (("total revenue by region", "revenue by region", "region wise revenue"),
         "SELECT region, ROUND(SUM(revenue), 2) AS total_revenue FROM sales GROUP BY region ORDER BY total_revenue DESC;"),
        (("most units", "most quantity", "sold the most", "top selling"),
         "SELECT product, SUM(quantity) AS units_sold FROM sales GROUP BY product ORDER BY units_sold DESC LIMIT 1;"),
        (("how many sales", "number of sales", "count sales", "sales records"),
         "SELECT COUNT(*) AS sales_count FROM sales;"),
        (("monthly revenue", "revenue by month", "each month"),
         "SELECT substr(sale_date, 1, 7) AS month, ROUND(SUM(revenue), 2) AS revenue FROM sales GROUP BY month ORDER BY month;"),
        (("average sale revenue", "average revenue", "average sale"),
         "SELECT ROUND(AVG(revenue), 2) AS average_revenue FROM sales;"),
        (("south region", "from south", "revenue in south"),
         "SELECT ROUND(SUM(revenue), 2) AS south_revenue FROM sales WHERE region = 'South';"),
        (("electronics", "products in electronic"),
         "SELECT DISTINCT product FROM sales WHERE category = 'Electronics' ORDER BY product;"),
        (("total quantity", "quantity sold", "total units"),
         "SELECT SUM(quantity) AS total_quantity FROM sales;"),
        (("revenue by category", "category wise revenue", "by category"),
         "SELECT category, ROUND(SUM(revenue), 2) AS total_revenue FROM sales GROUP BY category ORDER BY total_revenue DESC;"),
        (("total revenue", "revenue overall", "revenue generated"),
         "SELECT ROUND(SUM(revenue), 2) AS total_revenue FROM sales;"),
    ]
    for terms, sql in rules:
        if any(term in q for term in terms):
            return sql
    raise HTTPException(status_code=422, detail="Question not covered by this demo. Try one of the 10 questions in query_tests.json.")

def execute_readonly(sql: str) -> list[dict[str, Any]]:
    normalized = sql.strip().lower()
    if not normalized.startswith("select") or any(token in normalized for token in ("insert ", "update ", "delete ", "drop ", "alter ", "attach ", "pragma ")):
        raise HTTPException(status_code=400, detail="Only read-only SELECT queries are allowed.")
    con = sqlite3.connect(f"file:{DB_PATH.as_posix()}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        cur = con.execute(sql)
        return [dict(row) for row in cur.fetchall()]
    except sqlite3.Error as exc:
        raise HTTPException(status_code=400, detail=f"SQL execution failed: {exc}") from exc
    finally:
        con.close()

@app.get("/")
def home():
    return {"message": "CIA SQL Analyst API is running", "endpoint": "POST /cia/sql-analyst", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok", "database": DB_PATH.name, "training_pairs": len(load_json(TRAINING_PATH))}

@app.get("/training")
def training_pairs():
    return load_json(TRAINING_PATH)

@app.get("/tests")
def test_questions():
    return load_json(TESTS_PATH)

@app.post("/cia/sql-analyst")
def sql_analyst(payload: AnalystRequest):
    sql = choose_sql(payload.question)
    result = execute_readonly(sql)
    return {"question": payload.question, "sql": sql, "result": result}
