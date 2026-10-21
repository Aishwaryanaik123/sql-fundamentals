# Groq EDA Executive Report

## Included
- `Groq_EDA_Executive_Report.ipynb` — end-to-end notebook
- `data/sample_sales.csv` — sample dataset for immediate testing
- `outputs/` — folder for generated reports
- `WORKLOG.md` — practical-task worklog
- `TOOLS_USED.txt` — tools list

## Run with no local setup
1. Open Google Colab: https://colab.research.google.com/
2. Upload `Groq_EDA_Executive_Report.ipynb`.
3. Run the notebook cells from top to bottom.
4. Upload your CSV when prompted.
5. Optionally enter a Groq API key for AI-generated text. If skipped, the notebook uses its built-in fallback summary.
6. Download the generated PowerPoint when prompted.

The notebook installs required packages automatically inside the notebook runtime. No local Python/Docker setup is required.

## Output
The notebook creates a PowerPoint with 7 slides:
1. Title / dataset overview
2–6. Five data insights
7. Recommendations and next steps

It also writes an EDA profile JSON, executive summary text, and five-insights text file.
