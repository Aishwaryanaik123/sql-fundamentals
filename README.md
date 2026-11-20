# AI Data Analyst Platform — Week 12 Day 5

**Track:** Data Analyst Intern 3M  
**Task:** 3M Capstone — AI Data Analyst Platform — Full Demo

## Project overview
A lightweight, locally running data analyst platform. Users can upload a CSV file, preview records, inspect data quality, view charts, and ask simple natural-language questions about the dataset.

## Features
- CSV upload and sample dataset mode
- Dataset overview: row count, column count, missing cells and duplicate rows
- Data preview and CSV download
- Column data types, missing-value profile and numerical summary
- Bar, line, scatter and histogram visualisations
- Local question-and-answer engine for common analytical questions
- No API key required; uploaded data is processed locally by the app

## Folder structure
```text
week-12-day-5-ai-data-analyst-platform/
├── app.py
├── analyst_engine.py
├── requirements.txt
├── README.md
├── data/
│   └── sales_data.csv
├── docs/
│   └── process_documentation.md
├── demo/
│   ├── demo_checklist.md
│   └── demo_script.md
└── git_commands.md
```

## Run the project (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py -m streamlit run app.py
```
Open the local URL printed in the terminal (usually `http://localhost:8501`).

## Demo questions
Use the included sample dataset and try:
- What is the total Sales?
- What is the average Profit?
- Which Category is most common?
- What is the highest Quantity?
- Show missing values.
- How many rows are in the dataset?

## Limitations
The question engine supports common analytical intents and exact column names. It is a demonstration implementation, not a general-purpose large language model. More complex questions may need a dedicated LLM, semantic query layer, or SQL generation with validation.

## Learning outcome
Demonstrates an end-to-end analyst workflow: data ingestion, data quality inspection, exploratory analysis, visualisation, question answering, documentation and Git version control.
