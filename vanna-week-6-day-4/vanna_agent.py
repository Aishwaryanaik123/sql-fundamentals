from pathlib import Path
import os
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Vanna CIA SQL Analyst API")

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "sales.db"

class SQLAnalystRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {
        "service": "Vanna CIA SQL Analyst",
        "endpoint": "POST /cia/sql-analyst"
    }

@app.post("/cia/sql-analyst")
def sql_analyst(request: SQLAnalystRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    # This endpoint is structured for Vanna integration.
    # The SQL generation step should be connected to the configured Vanna Agent.
    # A safe demo mapping is included so the endpoint can be inspected without
    # requiring an LLM call.

    q = request.question.lower()

    demo_sql = {
        "how many sales records are there?":
            "SELECT COUNT(*) AS total_records FROM sales;",
        "what is the total sales revenue?":
            "SELECT SUM(quantity * unit_price) AS total_revenue FROM sales;",
        "what is the average unit price?":
            "SELECT AVG(unit_price) AS average_unit_price FROM sales;",
        "how many units were sold in bangalore?":
            "SELECT SUM(quantity) AS total_units FROM sales WHERE region = 'Bangalore';",
        "what is the revenue by product?":
            "SELECT product, SUM(quantity * unit_price) AS revenue FROM sales GROUP BY product ORDER BY revenue DESC;",
    }

    sql = demo_sql.get(q)

    if sql is None:
        return {
            "question": request.question,
            "sql": None,
            "message": "Connect this request to the configured Vanna Agent for dynamic NL-to-SQL generation."
        }

    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        rows = [dict(row) for row in conn.execute(sql).fetchall()]
        conn.close()
        return {
            "question": request.question,
            "sql": sql,
            "results": rows
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("vanna_agent:app", host="127.0.0.1", port=8000, reload=True)
