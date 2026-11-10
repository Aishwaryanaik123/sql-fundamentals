# Sales Forecasting Dashboard — Week 10 Day 5

## Project overview
A complete demonstration project that explores monthly sales history, evaluates a forecasting baseline, and presents a 12-month sales outlook in an offline-ready interactive HTML dashboard.

## Open the dashboard (no installation)
1. Extract the ZIP file.
2. Open `reports/sales_forecasting_dashboard.html` in Chrome, Edge, Firefox, or another modern browser.
3. The dashboard works locally and does not require Python, Streamlit, Plotly, internet access, or package installation.

## Included files
- `data/monthly_sales.csv` — 84 months of synthetic monthly sales data (Jan 2019–Dec 2025).
- `reports/sales_forecasting_dashboard.html` — standalone interactive dashboard.
- `reports/12_month_sales_forecast.csv` — forecast for Jan–Dec 2026.
- `reports/model_evaluation_metrics.csv` — holdout MAE, RMSE, and MAPE.
- `reports/validation_predictions.csv` — actual vs predicted values for the 12-month holdout.
- `src/forecast_sales.py` — reproducible Python implementation using the standard library.
- `experiment_process.md` — methodology and process notes.
- `execution_notes.txt` — run summary and interpretation.
- `PROJECT_INFO.txt` — project metadata.

## Methodology
A linear trend model with calendar-month indicator variables captures the overall trend and recurring month-of-year effects. The final 12 historical months are held out for validation. The model is then refit on all 84 observations to produce the next 12 monthly forecasts.

## Evaluation
See `reports/model_evaluation_metrics.csv`. MAE and RMSE are expressed in sales units; MAPE is a percentage. Metrics describe only this synthetic demonstration dataset.

## Important limitation
All sales data are synthetic and generated for learning/demo purposes. They are not actual company, customer, or market records. The forecast range shown is an approximate error band based on validation RMSE, not a calibrated prediction interval. Real deployment should use cleaned business data, backtesting across multiple periods, and appropriate monitoring.

## Technology
Python standard library, CSV, HTML, CSS, JavaScript, Git, GitHub.
