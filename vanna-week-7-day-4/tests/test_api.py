from fastapi.testclient import TestClient
from app import app
import json
from pathlib import Path

client = TestClient(app)
root = Path(__file__).resolve().parents[1]
tests = json.loads((root / "test_queries.json").read_text(encoding="utf-8"))

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["sales_rows"] == 12
    assert r.json()["training_examples"] == 5

def test_all_ten_questions():
    for item in tests:
        r = client.post("/cia/sql-analyst", json={"question": item["question"]})
        assert r.status_code == 200, (item["question"], r.text)
        body = r.json()
        assert body["sql"].strip().rstrip(";") == item["expected_sql"].strip().rstrip(";")
        assert isinstance(body["rows"], list)

def test_reject_unknown_question():
    r = client.post("/cia/sql-analyst", json={"question": "Tell me a joke"})
    assert r.status_code == 422
