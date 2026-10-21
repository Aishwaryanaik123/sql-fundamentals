# Groq EDA Executive Report

A ready-to-run CSV → automated EDA → executive summary → PowerPoint workflow.

## Included
- `app/streamlit_app.py` — complete Streamlit application
- `sample_data/sales_data.csv` — sample dataset to test the workflow
- `requirements.txt` — dependencies
- `run_app.bat` — Windows launcher
- `.env.example` — optional Groq API key setup
- `outputs/` — place exported reports here

## Run on Windows
1. Install Python 3.10+ if it is not already installed.
2. Double-click `run_app.bat`.
3. Open the local Streamlit URL shown in the terminal.
4. Upload a CSV and click **Generate executive summary**.
5. Download the PowerPoint from the page.

## Groq API key (optional)
The app works without a key using a built-in fallback summary. To use Groq:
- Set the `GROQ_API_KEY` environment variable before launching, or add it to your environment.
- Never commit a real API key to GitHub.

## Git commit
From this folder, run:
```bash
git init
git add .
git commit -m "Build Groq EDA executive report workflow"
```

The folder is provided with all source files and a sample CSV. Dependencies are not bundled; `run_app.bat` installs them automatically when run.
