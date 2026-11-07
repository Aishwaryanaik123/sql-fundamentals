# Forecasting Dashboard — Plotly + Streamlit
**Data Analyst Intern 3M | Week 10 Day 4**

## Objective
Build an interactive forecasting dashboard that presents historical monthly sales, a future forecast, model evaluation metrics, and seasonality using Plotly and Streamlit.

## Ready-to-view dashboard
Open `reports/forecast_dashboard_preview.html` in a web browser for the interactive Plotly dashboard preview. Open `reports/seasonality_preview.html` to view the monthly seasonality chart. These HTML reports are self-contained and include Plotly.

## Project structure
- `data/monthly_sales.csv` — 84 monthly observations from January 2019 through December 2025.
- `src/streamlit_app.py` — Streamlit dashboard source with Plotly charts, forecast horizon control, metrics, and CSV download.
- `reports/forecast_dashboard_preview.html` — interactive browser dashboard preview.
- `reports/seasonality_preview.html` — interactive seasonality chart.
- `reports/forecast_output.csv` — 12-month forecast with approximate residual bands.
- `reports/evaluation_metrics.csv` — holdout MAE and RMSE.
- `experiment_process.md` — process documentation.
- `execution_notes.txt` — execution summary and limitations.

## Forecasting approach
A transparent regression baseline is used: a linear time trend plus calendar-month indicator variables. The last 12 observations are held out for evaluation. The model is then refitted on all observations to create a 12-month forecast. The shaded range is an approximate ±1.96 residual-standard-deviation band, not a calibrated prediction interval.

## Evaluation results
- Holdout MAE: **5.03**
- Holdout RMSE: **6.05**

## Streamlit app
The source is provided in `src/streamlit_app.py`. To run it in an environment with dependencies installed:
```bash
python -m pip install -r requirements.txt
streamlit run src/streamlit_app.py
```

## Important limitation
The supplied sales dataset is synthetic and created for this educational task; it is not official Indian market data or live business data. Forecasts and evaluation metrics are demonstration outputs and should not be used for business decisions. The Streamlit app source is included, while the self-contained HTML preview is ready to open without installing Streamlit.
