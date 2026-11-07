from pathlib import Path
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "monthly_sales.csv"

st.set_page_config(page_title="Forecasting Dashboard", page_icon="📈", layout="wide")
st.title("📈 Monthly Sales Forecasting Dashboard")
st.caption("Plotly + Streamlit | Data Analyst Intern 3M — Week 10 Day 4")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
    return df.sort_values("date").reset_index(drop=True)

def make_design(dates, start_idx):
    dates = pd.to_datetime(pd.Series(dates))
    idx = np.arange(start_idx, start_idx + len(dates))
    month_dummies = np.column_stack([(dates.dt.month.values == m).astype(float) for m in range(2, 13)])
    return np.column_stack([np.ones(len(idx)), idx, month_dummies])

def fit_forecast(df, horizon):
    X = make_design(df["date"], 0)
    y = df["sales"].to_numpy()
    coefficients = np.linalg.lstsq(X, y, rcond=None)[0]
    fitted = X @ coefficients
    residual_std = float(np.std(y - fitted, ddof=1))
    future_dates = pd.date_range(df["date"].max() + pd.offsets.MonthBegin(1), periods=horizon, freq="MS")
    future_X = make_design(future_dates, len(df))
    predicted = future_X @ coefficients
    forecast = pd.DataFrame({
        "date": future_dates,
        "forecast": predicted,
        "lower_approx": predicted - 1.96 * residual_std,
        "upper_approx": predicted + 1.96 * residual_std,
    })
    return forecast, fitted

df = load_data()
horizon = st.sidebar.slider("Forecast horizon (months)", min_value=3, max_value=24, value=12)
forecast, fitted = fit_forecast(df, horizon)

# Last-12-month holdout evaluation, independent of future forecast
train, test = df.iloc[:-12], df.iloc[-12:]
holdout_beta = np.linalg.lstsq(make_design(train["date"], 0), train["sales"].to_numpy(), rcond=None)[0]
holdout_pred = make_design(test["date"], len(train)) @ holdout_beta
mae = float(np.mean(np.abs(test["sales"].to_numpy() - holdout_pred)))
rmse = float(np.sqrt(np.mean((test["sales"].to_numpy() - holdout_pred) ** 2)))

c1, c2, c3, c4 = st.columns(4)
c1.metric("Historical records", f"{len(df):,}")
c2.metric("Latest monthly sales", f"{df['sales'].iloc[-1]:,.1f}")
c3.metric("Holdout MAE", f"{mae:,.2f}")
c4.metric("Holdout RMSE", f"{rmse:,.2f}")

fig = go.Figure()
fig.add_trace(go.Scatter(x=df["date"], y=df["sales"], mode="lines+markers", name="Actual sales"))
fig.add_trace(go.Scatter(x=forecast["date"], y=forecast["forecast"], mode="lines+markers", name="Forecast",
                         line=dict(dash="dash", width=3)))
fig.add_trace(go.Scatter(x=list(forecast["date"]) + list(forecast["date"][::-1]),
                         y=list(forecast["upper_approx"]) + list(forecast["lower_approx"][::-1]),
                         fill="toself", fillcolor="rgba(99,110,250,0.15)",
                         line=dict(color="rgba(255,255,255,0)"), name="Approx. 95% residual band",
                         hoverinfo="skip"))
fig.update_layout(template="plotly_white", title="Historical Sales and Forecast",
                  xaxis_title="Month", yaxis_title="Sales units", hovermode="x unified")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Forecast values")
display = forecast.copy()
display["date"] = display["date"].dt.strftime("%Y-%m")
st.dataframe(display.round(2), use_container_width=True, hide_index=True)
st.download_button("Download forecast CSV", forecast.to_csv(index=False).encode("utf-8"),
                   file_name="forecast_output.csv", mime="text/csv")

st.subheader("Average sales by calendar month")
seasonality = df.assign(month=df["date"].dt.month).groupby("month", as_index=False)["sales"].mean()
season_fig = go.Figure(go.Bar(x=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
                              y=seasonality["sales"]))
season_fig.update_layout(template="plotly_white", xaxis_title="Month", yaxis_title="Average sales")
st.plotly_chart(season_fig, use_container_width=True)

st.info("Educational demonstration using synthetic sales data. The forecast uses a linear trend plus calendar-month effects. The shaded band is an approximate residual band, not a calibrated prediction interval.")
