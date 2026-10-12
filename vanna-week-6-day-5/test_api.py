import json
from pathlib import Path
from fastapi.testclient import TestClient
from app import app

ROOT = Path(__file__).resolve().parent
client = TestClient(app)
tests = json.loads((ROOT / "query_tests.json").read_text(encoding="utf-8"))
passed = 0
for i, item in enumerate(tests, 1):
    response = client.post("/cia/sql-analyst", json={"question": item["question"]})
    assert response.status_code == 200, (item["question"], response.text)
    body = response.json()
    assert body["sql"].strip().rstrip(";").lower() == item["sql"].strip().rstrip(";").lower(), item["question"]
    assert isinstance(body["result"], list)
    print(f"PASS {i}/10: {item['question']} -> {len(body['result'])} result row(s)")
    passed += 1
print(f"\n{passed}/10 natural-language tests passed.")
