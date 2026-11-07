# Experiment Process – Prophet Forecasting

## 1. Business context
A retail analyst may estimate near-term monthly demand and understand recurring seasonal patterns. This project demonstrates the workflow on Indian-market-style monthly sales data.

## 2. Data preparation
- Loaded monthly observations with `ds` as the date column and `y` as the target.
- Sorted chronologically and checked required fields and missing values.
- Dataset period: January 2019–December 2025 (84 monthly observations).

## 3. Exploratory analysis
- Reviewed the overall direction of the series.
- Examined annual seasonality and festive-period uplift.
- Considered a temporary disruption represented in the synthetic 2020 observations.

## 4. Prophet modeling design
- Yearly seasonality enabled.
- Weekly and daily seasonality disabled because observations are monthly.
- Additive seasonality selected for this demonstration.
- Final 12 months reserved for chronological holdout testing.

## 5. Evaluation and forecasting
The Python script calculates MAE and RMSE on the holdout period, refits Prophet on all observations, and forecasts the next 12 months.

## 6. Generated outputs after actual execution
- `reports/model_evaluation_metrics.csv`
- `reports/prophet_12_month_forecast.csv`
- `reports/prophet_forecast.png`
- `reports/prophet_components.png`

## 7. Limitations
The dataset is synthetic, not a verified official Indian market data source. The included HTML and CSV preview are illustrative; no Prophet model was fitted during package preparation. Forecast quality on real data depends on data quality, business context, structural changes, and validation.
