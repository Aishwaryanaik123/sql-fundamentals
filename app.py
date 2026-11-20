import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from analyst_engine import answer_question, build_profile

st.set_page_config(page_title="AI Data Analyst Platform", page_icon="📊", layout="wide")
st.title("📊 AI Data Analyst Platform")
st.caption("Upload a dataset, explore key insights, and ask questions in plain English.")

uploaded = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
if uploaded:
    try:
        df = pd.read_csv(uploaded)
    except Exception as exc:
        st.error(f"Could not read this CSV: {exc}")
        st.stop()
else:
    sample_path = Path(__file__).parent / "data" / "sales_data.csv"
    df = pd.read_csv(sample_path)
    st.sidebar.info("Showing the included sample sales dataset. Upload your own CSV to analyse it.")

if df.empty:
    st.warning("The selected dataset has no rows.")
    st.stop()

st.sidebar.write(f"**Rows:** {len(df):,}  |  **Columns:** {len(df.columns)}")
st.subheader("Dataset overview")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Rows", f"{len(df):,}")
c2.metric("Columns", f"{len(df.columns):,}")
c3.metric("Missing cells", f"{int(df.isna().sum().sum()):,}")
c4.metric("Duplicate rows", f"{int(df.duplicated().sum()):,}")

tab1, tab2, tab3, tab4 = st.tabs(["Data preview", "Data profile", "Visualisations", "Ask the analyst"])
with tab1:
    st.dataframe(df, use_container_width=True, height=350)
    st.download_button("Download current dataset", df.to_csv(index=False).encode("utf-8"),
                       "analysed_dataset.csv", "text/csv")
with tab2:
    profile = build_profile(df)
    left, right = st.columns(2)
    with left:
        st.markdown("**Column data types**")
        st.dataframe(profile["types"], use_container_width=True)
    with right:
        st.markdown("**Missing values**")
        st.dataframe(profile["missing"], use_container_width=True)
    numeric = df.select_dtypes(include="number")
    if not numeric.empty:
        st.markdown("**Numerical summary**")
        st.dataframe(numeric.describe().T, use_container_width=True)
    else:
        st.info("No numerical columns found.")
with tab3:
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    all_cols = df.columns.tolist()
    if numeric_cols:
        xcol = st.selectbox("Category / X-axis", all_cols, index=0, key="x")
        ycol = st.selectbox("Numeric / Y-axis", numeric_cols, key="y")
        chart_type = st.selectbox("Chart type", ["Bar", "Line", "Scatter", "Histogram"])
        if chart_type == "Bar":
            grouped = df.groupby(xcol, dropna=False)[ycol].sum().reset_index().head(30)
            fig = px.bar(grouped, x=xcol, y=ycol, title=f"{ycol} by {xcol}")
        elif chart_type == "Line":
            grouped = df.groupby(xcol, dropna=False)[ycol].sum().reset_index().head(100)
            fig = px.line(grouped, x=xcol, y=ycol, title=f"{ycol} by {xcol}")
        elif chart_type == "Scatter":
            fig = px.scatter(df, x=xcol, y=ycol, title=f"{ycol} vs {xcol}")
        else:
            fig = px.histogram(df, x=ycol, title=f"Distribution of {ycol}")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Visualisations need at least one numerical column.")
with tab4:
    st.markdown("Ask questions such as **What is the total Sales?**, **Which Category has the highest Profit?**, or **Show average Quantity**.")
    question = st.text_input("Enter your question")
    if st.button("Analyse", type="primary") and question.strip():
        result = answer_question(df, question)
        st.markdown("**Analyst response**")
        st.write(result)
    st.caption("This demo uses a transparent local question engine; it does not send your data to an external AI service.")
