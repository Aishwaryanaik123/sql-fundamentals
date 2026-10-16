# CIA Data Analyst Mode — CSV + PandasAI starter

A small Flask web app for the practical task:
1. Upload and validate a CSV file.
2. Parse it with Pandas and keep it in a temporary server folder tied to the browser session.
3. Send a natural-language question to a `/api/query` endpoint.
4. Return an answer plus Plotly figure JSON and render the chart in the frontend.

## Requirements
- Python 3.10+
- Internet connection for frontend CDN libraries
- A PandasAI API key for full natural-language AI queries

## Run on Windows PowerShell

```powershell
cd cia_data_analyst_mode
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
$env:CIA_SECRET_KEY = "replace-with-a-long-random-secret"
$env:PANDASAI_API_KEY = "your-pandasai-api-key"
python app.py
```

Open http://127.0.0.1:5000

If you do not set `PANDASAI_API_KEY`, the app uses a small Pandas fallback for basic count, column, average, and summary questions. This fallback is for testing only and is not a full natural-language query engine.

## Test with 5 questions
Upload a CSV, then try:
1. How many rows are in this dataset?
2. What columns are available?
3. What is the average?
4. Summarize the dataset.
5. Show me a preview of the data.

## API
- `POST /api/upload` — multipart form field named `file`
- `POST /api/query` — JSON body such as `{"question":"What is the average salary?"}`

The query response includes `answer`, `chart_json`, `engine`, and optional `note`.

## Security notes
- 10 MB upload limit, `.csv` extension allowlist, sanitized filename, row/column limits.
- CSV cells are treated as data and never executed.
- For production, add authentication, CSRF protection, rate limiting, a stronger secret, file-content/MIME validation, and scheduled cleanup of abandoned temporary uploads. Do not expose this development server publicly.
- This is a starter implementation; review current PandasAI package/API requirements for the version you install.
