# Groq EDA Executive Report

A ready-to-run mini project that accepts a CSV, performs exploratory data analysis,
creates five descriptive insights, generates an approximately 200-word executive summary,
and exports a 7-slide PowerPoint (title + five insights + recommendations).

## Included
- `app.py` — complete Streamlit application
- `data/sample_sales.csv` — sample dataset to test the workflow
- `requirements.txt` — dependencies
- `output/` — destination for generated PowerPoint files

## Quick start
The folder is prepared, but Python packages must be available in the environment where
the app runs. To avoid installing anything on your computer, upload the folder to a hosted
Python environment such as Google Colab or Streamlit Community Cloud and follow that
platform's run/deploy steps.

For Groq-generated summaries, set the `GROQ_API_KEY` environment variable in the hosting
platform's secrets/settings. The app still produces a template-based summary if no key is
configured. Never put an API key directly in a public repository.

## PowerPoint
Open the app, upload a CSV (or load the included sample), review the insights and summary,
then click **Generate PowerPoint** to download the presentation.

## Notes
- The five insights are descriptive and based on the uploaded data; they are not causal claims.
- The local fallback summary does not call Groq.
- The generated deck contains a title slide, five insight slides, a summary slide, and a
  recommendations slide (8 slides total).
