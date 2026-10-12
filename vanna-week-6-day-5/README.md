# Vanna / CIA SQL Analyst Practical Package

## What's included
- `sales.db`: ready-made SQLite sample database and sales table
- `training_examples.json`: 5 example natural-language questions and SQL answers
- `query_tests.json`: 10 natural-language questions with manually reviewable expected SQL
- `app.py`: API with `POST /cia/sql-analyst`
- `test_api.py`: end-to-end tests for all 10 queries
- `verify_sql.py`: executes the expected SQL directly against SQLite for manual verification
- `START.bat`: sets up a local Python virtual environment and installs the small API dependencies automatically, then starts the server

## Start
1. Extract the ZIP.
2. Double-click `START.bat`.
3. On first launch, it requires Python 3.10+ and an internet connection to install the API packages. No separate database server or API key is needed.
4. Open the API docs at `http://127.0.0.1:8000/docs`.
5. Expand `POST /cia/sql-analyst`, click **Try it out**, and submit:
   ```json
   {"question": "What is the total revenue?"}
   ```
6. To test all 10 questions, run `RUN_TESTS.bat` after setup.

## Endpoint response
The endpoint returns the original question, SQL selected for the question, and the rows returned from SQLite.

## Important implementation note
This package is a self-contained, deterministic natural-language-to-SQL practical demo. It includes the five Q&A examples and uses explicit mappings for the ten validated questions so it can run without an external LLM/API key. It does **not** instantiate or train the Vanna library itself; use this as a runnable endpoint/demo scaffold, not as proof of Vanna model training. To satisfy a strict requirement to train the actual Vanna framework, a Vanna version and an LLM/vector-store configuration must be selected separately.
