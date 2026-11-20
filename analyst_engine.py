import pandas as pd
import re

def build_profile(df):
    types = pd.DataFrame({"Column": df.columns, "Data type": [str(x) for x in df.dtypes]})
    missing = pd.DataFrame({
        "Column": df.columns,
        "Missing count": [int(df[c].isna().sum()) for c in df.columns],
        "Missing %": [round(float(df[c].isna().mean() * 100), 2) for c in df.columns]
    }).sort_values("Missing count", ascending=False)
    return {"types": types, "missing": missing}

def _find_column(df, question):
    q = question.lower()
    for col in df.columns:
        if col.lower() in q:
            return col
    # Common singular/plural matching
    words = re.findall(r"[a-zA-Z_]+", q)
    for col in df.columns:
        c = col.lower()
        if c in words or c.rstrip("s") in words:
            return col
    return None

def answer_question(df, question):
    q = question.lower()
    numeric = df.select_dtypes(include="number").columns.tolist()
    col = _find_column(df, question)

    if any(k in q for k in ["missing", "null", "empty"]):
        missing = df.isna().sum().sort_values(ascending=False)
        return "Missing values by column:\\n" + missing.to_string()

    if any(k in q for k in ["duplicate", "duplicates"]):
        return f"The dataset contains {int(df.duplicated().sum())} duplicate rows."

    if any(k in q for k in ["how many rows", "number of rows", "row count", "records"]):
        return f"The dataset contains {len(df):,} rows and {len(df.columns)} columns."

    if col is None and numeric:
        col = numeric[0]
    if col is None:
        return "I could not identify a column. Try including an exact column name from the dataset."

    if col in numeric:
        s = df[col].dropna()
        if s.empty:
            return f"Column '{col}' has no numeric values to analyse."
        if any(k in q for k in ["average", "mean"]):
            return f"Average {col}: {s.mean():,.2f}"
        if any(k in q for k in ["highest", "maximum", "max", "largest"]):
            return f"Highest {col}: {s.max():,.2f}"
        if any(k in q for k in ["lowest", "minimum", "min", "smallest"]):
            return f"Lowest {col}: {s.min():,.2f}"
        if any(k in q for k in ["count", "how many"]):
            return f"Non-empty values in {col}: {int(s.count()):,}"
        if any(k in q for k in ["total", "sum"]):
            return f"Total {col}: {s.sum():,.2f}"
        return f"Summary for {col}: total = {s.sum():,.2f}, average = {s.mean():,.2f}, minimum = {s.min():,.2f}, maximum = {s.max():,.2f}."

    if any(k in q for k in ["most common", "top", "highest", "popular", "frequent"]):
        counts = df[col].value_counts(dropna=False)
        if counts.empty:
            return f"No values found in {col}."
        return f"Most frequent {col}: {counts.index[0]} ({int(counts.iloc[0])} records).\\n\\nTop values:\\n{counts.head(10).to_string()}"
    return f"Column '{col}' contains {df[col].nunique(dropna=True)} unique values. Most frequent values:\\n{df[col].value_counts(dropna=False).head(10).to_string()}"
