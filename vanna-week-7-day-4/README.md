# Vanna / CIA SQL Analyst Practical — Ready Package

## Included
- `data/sales.db`: sample SQLite database with 12 sales rows.
- `training_examples.json`: 5 question-to-SQL examples.
- `test_queries.json`: 10 natural-language questions with expected SQL for manual verification.
- `app.py`: FastAPI service exposing `POST /cia/sql-analyst`.
- `tests/test_api.py`: automated checks for all 10 questions and the health endpoint.
- `START.bat`: creates a local virtual environment, downloads Python dependencies, and starts the API.
- `RUN_TESTS.bat`: runs tests after the first setup.

## Important transparency note
This package is a runnable, self-contained **API demo** with a deterministic question matcher and manually verified SQL examples. It does **not** install or run the Vanna library, does not call an LLM, and therefore should not be submitted as proof of genuine Vanna model training. The endpoint is compatible with the requested path and demonstrates the database/API/test workflow. Genuine Vanna training requires choosing/configuring a Vanna version and an LLM/database integration.

## How to run on Windows
1. Extract this ZIP.
2. Double-click `START.bat`.
3. On first run, it requires Python 3.10+ already installed and an internet connection to download FastAPI/Uvicorn/test dependencies. It performs the package setup automatically; you do not need to type commands.
4. Open `http://127.0.0.1:8000/docs`.
5. Expand `POST /cia/sql-analyst`, click **Try it out**, and send:
   `{"question":"What is the total revenue from completed sales?"}`
6. For health status, open `http://127.0.0.1:8000/health`.
7. Stop the server with `Ctrl+C` in the terminal window.

## Verify the 10 queries
Compare each `expected_sql` in `test_queries.json` with the SQL returned by the API. Then run `RUN_TESTS.bat` to check the 10 expected SQL statements end-to-end.

## Example request
```json
{
  "question": "What is the total revenue from completed sales?"
}
```

## Example endpoint
`POST http://127.0.0.1:8000/cia/sql-analyst`

## Dependencies
Python 3.10+ and internet for first-time dependency download. No separate database server or API key is needed for this demo.
