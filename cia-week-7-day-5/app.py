import os
import uuid
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.io as pio
from flask import Flask, jsonify, request, send_from_directory, session
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder="static")
app.secret_key = os.environ.get("CIA_SECRET_KEY", "change-this-development-secret")
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB upload limit
UPLOAD_DIR = Path("temp_uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
ALLOWED_EXTENSIONS = {".csv"}

# Optional PandasAI integration. Set PANDASAI_API_KEY to enable it.
def ask_pandasai(df: pd.DataFrame, question: str):
    api_key = os.environ.get("PANDASAI_API_KEY")
    if not api_key:
        return None, "PandasAI is not enabled: set PANDASAI_API_KEY to use the AI query engine."
    try:
        from pandasai import Agent
        agent = Agent(df, config={"api_key": api_key, "verbose": False})
        answer = agent.chat(question)
        return str(answer), None
    except Exception as exc:
        return None, f"PandasAI query failed: {exc}"

def safe_load_csv(path: Path) -> pd.DataFrame:
    # Read only tabular data; do not execute anything contained in cells.
    df = pd.read_csv(path, nrows=100_000)
    if df.empty:
        raise ValueError("The CSV has no data rows.")
    if len(df.columns) > 100:
        raise ValueError("CSV has too many columns (maximum 100).")
    return df

def make_chart(df: pd.DataFrame, question: str):
    """Create a useful chart from the first suitable numeric column."""
    numeric = df.select_dtypes(include="number").columns.tolist()
    if not numeric:
        return None
    # Prefer a categorical column for the x-axis; otherwise use row index.
    categorical = [c for c in df.columns if c not in numeric]
    y = numeric[0]
    if categorical:
        x = categorical[0]
        chart_df = df[[x, y]].dropna().head(100)
        fig = px.bar(chart_df, x=x, y=y, title=f"{y} by {x}")
    else:
        chart_df = df[[y]].dropna().head(100).reset_index()
        fig = px.line(chart_df, x="index", y=y, title=f"{y} by row")
    return pio.to_json(fig, pretty=False)

def basic_pandas_answer(df: pd.DataFrame, question: str) -> str:
    """Safe no-key fallback for quick testing; not a full natural-language engine."""
    q = question.lower()
    if "how many" in q or "count" in q or "number of rows" in q:
        return f"The dataset contains {len(df):,} rows and {len(df.columns)} columns."
    if "column" in q or "fields" in q:
        return "Columns: " + ", ".join(map(str, df.columns))
    numeric = df.select_dtypes(include="number")
    if "average" in q or "mean" in q:
        if numeric.empty:
            return "There are no numeric columns to average."
        col = next((c for c in numeric.columns if str(c).lower() in q), numeric.columns[0])
        return f"Average of {col}: {numeric[col].mean():,.3f}"
    if "summary" in q or "describe" in q:
        return numeric.describe().round(3).to_string() if not numeric.empty else df.describe(include="all").to_string()
    return ("Preview of the dataset (first 5 rows):\n" +
            df.head(5).to_string(index=False) +
            "\n\nFor full natural-language analysis, configure PANDASAI_API_KEY.")

@app.get("/")
def index():
    return send_from_directory("static", "index.html")

@app.post("/api/upload")
def upload_csv():
    if "file" not in request.files:
        return jsonify(error="Choose a CSV file."), 400
    file = request.files["file"]
    if not file.filename:
        return jsonify(error="Choose a CSV file."), 400
    filename = secure_filename(file.filename)
    if Path(filename).suffix.lower() not in ALLOWED_EXTENSIONS:
        return jsonify(error="Only .csv files are allowed."), 400
    upload_id = str(uuid.uuid4())
    path = UPLOAD_DIR / f"{upload_id}.csv"
    try:
        file.save(path)
        df = safe_load_csv(path)
    except Exception as exc:
        path.unlink(missing_ok=True)
        return jsonify(error=f"Could not read CSV: {exc}"), 400

    # Keep the uploaded file scoped to this browser session.
    old_id = session.get("upload_id")
    if old_id:
        (UPLOAD_DIR / f"{old_id}.csv").unlink(missing_ok=True)
    session["upload_id"] = upload_id
    return jsonify(
        message="CSV uploaded successfully.",
        rows=int(len(df)),
        columns=[str(c) for c in df.columns],
        preview=df.head(10).where(pd.notna(df.head(10)), None).to_dict(orient="records")
    )

@app.post("/api/query")
def query_csv():
    body = request.get_json(silent=True) or {}
    question = str(body.get("question", "")).strip()
    if not question:
        return jsonify(error="Enter a question."), 400
    upload_id = session.get("upload_id")
    if not upload_id:
        return jsonify(error="Upload a CSV first."), 400
    path = UPLOAD_DIR / f"{upload_id}.csv"
    if not path.exists():
        session.pop("upload_id", None)
        return jsonify(error="Your temporary upload has expired. Please upload again."), 400
    try:
        df = safe_load_csv(path)
    except Exception as exc:
        return jsonify(error=f"Could not load CSV: {exc}"), 400

    answer, ai_error = ask_pandasai(df, question)
    if answer is None:
        answer = basic_pandas_answer(df, question)
    return jsonify(
        answer=answer,
        chart_json=make_chart(df, question),
        engine="PandasAI" if ai_error is None else "Pandas fallback",
        note=ai_error
    )

@app.errorhandler(413)
def too_large(_error):
    return jsonify(error="File is too large. Maximum upload size is 10 MB."), 413

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
