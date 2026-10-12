import json, sqlite3
from pathlib import Path
ROOT = Path(__file__).resolve().parent
tests = json.loads((ROOT / "query_tests.json").read_text(encoding="utf-8"))
con = sqlite3.connect(ROOT / "sales.db")
try:
    for i, item in enumerate(tests, 1):
        rows = con.execute(item["sql"]).fetchall()
        print(f"{i}. {item['question']}\n   SQL: {item['sql']}\n   Result: {rows}\n")
finally:
    con.close()
