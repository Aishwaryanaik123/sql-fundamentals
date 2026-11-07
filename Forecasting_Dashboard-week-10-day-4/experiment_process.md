# Experiment Process — Week 10 Day 4

## 1. Data preparation
Prepared 84 monthly synthetic sales observations from January 2019 to December 2025. Parsed dates, sorted chronologically, and checked the dataset shape and numeric sales field.

## 2. Forecasting method
Implemented a regression baseline using a linear time index and calendar-month indicator variables. This provides a trend component and recurring month-of-year effects. The last 12 months were held out for a chronological evaluation; no random train/test split was used.

## 3. Evaluation
Predicted the held-out 12 months and calculated mean absolute error (MAE) and root mean squared error (RMSE). The model was then refitted using the full dataset to produce the next 12 monthly forecast values.

## 4. Dashboard design
Created a Streamlit dashboard source with:
- Sidebar control for forecast horizon (3–24 months)
- KPI metrics for record count, latest sales, holdout MAE, and RMSE
- Plotly historical-versus-forecast line chart
- Approximate residual range
- Forecast data table and CSV download
- Average sales by calendar month chart

## 5. Deliverables
Generated a self-contained interactive Plotly HTML preview, a seasonality preview, forecast CSV, evaluation metrics CSV, Streamlit app source, and documentation.

## 6. Interpretation and limitations
This is a synthetic educational example. The model is a transparent trend-plus-seasonality baseline, not a tuned production forecasting system. The residual band is approximate and not a statistically calibrated prediction interval. Real deployment requires actual business data, backtesting across multiple cutoffs, and monitoring.
