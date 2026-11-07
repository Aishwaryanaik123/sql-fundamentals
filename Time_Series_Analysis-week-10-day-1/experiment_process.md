# Experiment Process – Week 10 Day 1

## 1. Understand the time series
The dataset contains monthly sales observations with a date column and a numeric sales value. It spans five years and is synthetic for learning purposes.

## 2. Identify trend
A line plot and 12-month rolling mean are used to inspect the long-term direction while smoothing short-term fluctuations.

## 3. Identify seasonality
Additive decomposition with a period of 12 separates the observed series into trend, seasonal, and residual components. A 12-month period is appropriate for monthly data when annual repetition is being examined.

## 4. Build an ARIMA baseline
The script uses ARIMA(1,1,1) as a baseline. The first differencing term (d=1) helps model a series whose level changes over time. The AR and MA terms capture short-term dependence.

## 5. Evaluate
The final 12 observed months are held out from model fitting. The script reports Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) for the holdout forecast.

## 6. Forecast
After holdout evaluation, the model is refitted on the full dataset and produces a 12-month forecast with confidence intervals.

## 7. Document limitations
The input is synthetic, and the offline report is illustrative. ARIMA(1,1,1) is a baseline choice, not a tuned optimum. Real forecasting requires data-quality checks, residual diagnostics, candidate-order comparison, and time-aware validation.
