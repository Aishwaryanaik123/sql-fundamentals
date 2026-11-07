"""Prophet forecasting workflow for synthetic Indian-market-style monthly sales data."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "indian_market_monthly_sales.csv"
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["ds"]).sort_values("ds")
if not {"ds", "y"}.issubset(df.columns):
    raise ValueError("Dataset must contain ds and y columns.")
if df[["ds", "y"]].isna().any().any():
    raise ValueError("Dataset contains missing ds/y values.")

train, test = df.iloc[:-12].copy(), df.iloc[-12:].copy()
model = Prophet(yearly_seasonality=True, weekly_seasonality=False,
                daily_seasonality=False, seasonality_mode="additive",
                changepoint_prior_scale=0.05)
model.fit(train)
holdout_future = model.make_future_dataframe(periods=12, freq="MS")
holdout_forecast = model.predict(holdout_future).tail(12)
mae = mean_absolute_error(test["y"], holdout_forecast["yhat"])
rmse = np.sqrt(mean_squared_error(test["y"], holdout_forecast["yhat"]))
pd.DataFrame([{"MAE": mae, "RMSE": rmse, "holdout_months": len(test)}]).to_csv(
    REPORTS / "model_evaluation_metrics.csv", index=False)

final_model = Prophet(yearly_seasonality=True, weekly_seasonality=False,
                      daily_seasonality=False, seasonality_mode="additive",
                      changepoint_prior_scale=0.05)
final_model.fit(df)
future = final_model.make_future_dataframe(periods=12, freq="MS")
forecast = final_model.predict(future)
forecast[["ds", "yhat", "yhat_lower", "yhat_upper", "trend"]].to_csv(
    REPORTS / "prophet_12_month_forecast.csv", index=False)

fig = final_model.plot(forecast)
fig.suptitle("Prophet – Monthly Indian Market-Style Sales Forecast", y=1.02)
fig.tight_layout()
fig.savefig(REPORTS / "prophet_forecast.png", dpi=160, bbox_inches="tight")
plt.close(fig)
fig = final_model.plot_components(forecast)
fig.tight_layout()
fig.savefig(REPORTS / "prophet_components.png", dpi=160, bbox_inches="tight")
plt.close(fig)

print("Prophet forecasting completed.")
print(f"Holdout MAE: {mae:.2f}")
print(f"Holdout RMSE: {rmse:.2f}")
print(f"Forecast saved to: {REPORTS / 'prophet_12_month_forecast.csv'}")
