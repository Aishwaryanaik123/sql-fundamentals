# Week 10 Day 1 – Time Series Analysis: Trends, Seasonality, ARIMA

## Objective
Analyze monthly observations to identify long-term trend and recurring seasonality, then demonstrate an ARIMA forecasting workflow.

## Included files
- `data/monthly_sales.csv` – 60 months of synthetic demonstration data (January 2021–December 2025).
- `src/time_series_analysis.py` – loads data, checks frequency, decomposes trend/seasonality, fits ARIMA, evaluates a holdout period, and saves forecast outputs.
- `reports/time_series_dashboard.html` – offline report with an illustrative trend/seasonality/forecast summary.
- `reports/sample_analysis.md` – interpretation and limitations.
- `experiment_process.md` – documented analysis workflow.
- `execution_notes.txt` – how to review and optionally run the project.
- `requirements.txt` – Python dependencies.

## Important data note
The supplied dataset is synthetic and generated for demonstration. The offline HTML report is an illustrative summary, not the output of an executed ARIMA fit. No live analysis or forecast was run while preparing this package. Running the script locally will perform the analysis on the included synthetic dataset and generate actual outputs.

## View without installation
Open `reports/time_series_dashboard.html` in Chrome or Edge. No installation is needed to view the report.

## Optional execution
Use Python 3.10 or newer.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python src/time_series_analysis.py
```

## Analysis performed by the script
1. Parse the date column and set a monthly time index.
2. Plot the original series and a 12-month rolling average.
3. Apply additive seasonal decomposition with a 12-month period.
4. Fit ARIMA(1,1,1) on the training portion.
5. Forecast the held-out final 12 months and calculate MAE and RMSE.
6. Refit ARIMA on the full series and forecast the next 12 months.
7. Save decomposition, forecast, and evaluation artifacts under `reports/generated/`.

## Interpretation caution
ARIMA order selection should be validated rather than assumed. Compare candidate orders, inspect residuals, and use time-aware validation before using forecasts for business decisions. The fixed ARIMA(1,1,1) model here is a teaching baseline, not a claim of optimality.
