# Week 10 Day 2 – Prophet Forecasting on Indian Market Data

## Objective
Build a reproducible time-series forecasting workflow using Prophet on Indian-market-style monthly retail sales data. The workflow covers date preparation, trend and seasonality analysis, model fitting, holdout evaluation, and future forecasting.

## Dataset
`data/indian_market_monthly_sales.csv` contains monthly observations from January 2019 through December 2025. **This is deterministic synthetic demonstration data, not official Indian market data, live NSE/BSE data, or actual company sales.** It demonstrates a long-term trend, annual seasonality, festive-period uplift, and a temporary 2020 disruption.

Columns: `ds` (month start date) and `y` (illustrative monthly sales index).

## Included
- `src/prophet_forecasting.py` – Prophet training, holdout evaluation, forecast generation, and chart export.
- `data/indian_market_monthly_sales.csv` – synthetic demonstration dataset.
- `reports/forecast_preview.html` – offline preview; no installation needed to view.
- `reports/sample_forecast_preview.csv` – illustrative forecast values, not actual Prophet output.
- `experiment_process.md` – methodology and interpretation.
- `execution_notes.txt` – run instructions.
- `requirements.txt` – dependencies.

## View without installing anything
Open `reports/forecast_preview.html` in Chrome or Edge.

## Run the actual Prophet model (optional)
Use Python 3.10 or newer:
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/prophet_forecasting.py
```
The script reserves the final 12 months for holdout testing, fits Prophet on earlier observations, evaluates MAE and RMSE, then refits on all observations and forecasts the next 12 months.

## Important execution note
The package is prepared for review. The offline preview uses illustrative values. **Prophet was not fitted and no live forecast metrics were generated while preparing this folder.** Running the script with the listed dependencies will perform the actual Prophet fit on the included synthetic dataset.

## Conclusion
This project demonstrates Prophet trend and yearly-seasonality modeling. Validate forecasts on real, approved data before business decisions. This demonstration is not investment advice.
