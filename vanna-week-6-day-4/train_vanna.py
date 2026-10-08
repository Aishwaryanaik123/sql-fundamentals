from pathlib import Path
import os

# Vanna 2.x integration
from vanna import Agent
from vanna.integrations.sqlite import SqliteRunner
from vanna.integrations.openai import OpenAIChat

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "sales.db"

# Set OPENAI_API_KEY before running the real Vanna agent.
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Set it before running the Vanna training script."
    )

llm = OpenAIChat(
    config={
        "api_key": api_key,
        "model": "gpt-5"
    }
)

runner = SqliteRunner(
    database_path=str(DB_PATH)
)

agent = Agent(
    llm=llm,
    tool_registry=runner
)

training_examples = [
    {
        "question": "What is the total number of sales records?",
        "sql": "SELECT COUNT(*) AS total_records FROM sales;"
    },
    {
        "question": "What is the total sales revenue?",
        "sql": "SELECT SUM(quantity * unit_price) AS total_revenue FROM sales;"
    },
    {
        "question": "What is the average unit price?",
        "sql": "SELECT AVG(unit_price) AS average_unit_price FROM sales;"
    },
    {
        "question": "How many units were sold in Bangalore?",
        "sql": "SELECT SUM(quantity) AS total_units FROM sales WHERE region = 'Bangalore';"
    },
    {
        "question": "What is the revenue by product?",
        "sql": "SELECT product, SUM(quantity * unit_price) AS revenue FROM sales GROUP BY product ORDER BY revenue DESC;"
    },
]

# Vanna versions can expose training through different APIs.
# Keep the examples in a portable form for the internship deliverable.
with open(BASE_DIR / "training_examples.txt", "w", encoding="utf-8") as f:
    for item in training_examples:
        f.write(f"Question: {item['question']}\nSQL: {item['sql']}\n\n")

print(f"Prepared {len(training_examples)} custom Q&A training examples.")
print(f"Database: {DB_PATH}")
