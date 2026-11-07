"""Time-series analysis: trend, annual seasonality, ARIMA baseline."""
from pathlib import Path
import json
import warnings

import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "monthly_sales.csv"
OUT = ROOT / "reports" / "generated"
OUT.mkdir(parents=True, exist_ok=True)


def main():
    warnings.filterwarnings("ignore")
    df = pd.read_csv(DATA, parse_dates=["date"])
    series = df.set_index("date")["sales"].asfreq("MS")

    # Trend inspection
    rolling = series.rolling(12).mean()
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(series, label="Monthly sales")
    ax.plot(rolling, label="12-month rolling mean", linewidth=2)
    ax.set_title("Monthly Sales and Smoothed Trend")
    ax.set_ylabel("Sales (synthetic units)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "trend.png", dpi=150)
    plt.close(fig)

    # Seasonal decomposition
    decomposition = seasonal_decompose(series, model="additive", period=12)
    fig = decomposition.plot()
    fig.set_size_inches(11, 8)
    fig.tight_layout()
    fig.savefig(OUT / "seasonal_decomposition.png", dpi=150)
    plt.close(fig)

    # Time-aware holdout evaluation: last 12 months are not used for fitting.
    train, test = series.iloc[:-12], series.iloc[-12:]
    model = ARIMA(train, order=(1, 1, 1)).fit()
    prediction = model.forecast(steps=len(test))
    mae = mean_absolute_error(test, prediction)
    rmse = mean_squared_error(test, prediction) ** 0.5

    holdout = pd.DataFrame({
        "actual": test,
        "forecast": prediction,
    })
    holdout.to_csv(OUT / "holdout_forecast.csv", index_label="date")

    # Refit on all observations and forecast the next year.
    final_model = ARIMA(series, order=(1, 1, 1)).fit()
    forecast_obj = final_model.get_forecast(steps=12)
    forecast = forecast_obj.predicted_mean
    interval = forecast_obj.conf_int()
    future = pd.DataFrame({
        "forecast": forecast,
        "lower_95": interval.iloc[:, 0],
        "upper_95": interval.iloc[:, 1],
    })
    future.to_csv(OUT / "next_12_month_forecast.csv", index_label="date")

    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(series, label="Observed")
    ax.plot(forecast, label="12-month forecast")
    ax.fill_between(
        forecast.index,
        interval.iloc[:, 0].to_numpy(),
        interval.iloc[:, 1].to_numpy(),
        alpha=0.2,
        label="95% confidence interval",
    )
    ax.set_title("ARIMA(1,1,1) – 12-Month Forecast")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "arima_forecast.png", dpi=150)
    plt.close(fig)

    metrics = {"model": "ARIMA(1,1,1)", "holdout_months": 12,
               "MAE": float(mae), "RMSE": float(rmse)}
    (OUT / "evaluation_metrics.json").write_text(
        json.dumps(metrics, indent=2), encoding="utf-8"
    )
    print("Time-series analysis complete.")
    print(json.dumps(metrics, indent=2))
    print(f"Generated files: {OUT}")


if __name__ == "__main__":
    main()
