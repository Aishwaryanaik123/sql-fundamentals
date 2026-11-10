# Experiment Process — Week 10 Day 5

1. **Define the objective:** create a sales forecasting dashboard that combines historical performance, seasonality, validation metrics, and a forward-looking forecast.
2. **Prepare data:** use 84 monthly observations from January 2019 through December 2025. The sample is synthetic and reproducible.
3. **Explore patterns:** review the monthly sales series and calculate average sales for each calendar month.
4. **Build baseline:** fit a linear trend with month-of-year indicator variables to represent trend and recurring seasonal differences.
5. **Validate:** train on the first 72 months and predict the final 12 months. Calculate MAE, RMSE, and MAPE.
6. **Forecast:** refit on all 84 months and generate forecasts for January–December 2026.
7. **Visualize:** create a self-contained HTML dashboard with historical and forecast lines, monthly averages, evaluation metrics, and a forecast table.
8. **Document:** save forecast data, validation predictions, metrics, limitations, and reproduction instructions.

## Interpretation
The model provides an interpretable baseline for demonstrating a forecasting workflow. Because the sample is synthetic and the validation window is a single 12-month period, its metrics should not be treated as evidence of production forecasting accuracy.
