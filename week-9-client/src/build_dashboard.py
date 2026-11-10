from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA, REPORTS = ROOT / "data", ROOT / "reports"
listings = pd.read_csv(DATA / "da_realestate_listings.csv")
customers = pd.read_csv(DATA / "da_customer_profiles.csv")
products = pd.read_csv(DATA / "da_product_catalogue.csv")
products["gross_margin_pct"] = np.where(products.MRP > 0, (products.MRP-products.COGS)/products.MRP*100, np.nan)

listings.groupby("city").agg(
    listings=("listing_id","count"), sold=("sold","sum"),
    sold_rate_pct=("sold",lambda s:s.mean()*100),
    median_price_lakh=("total_price_lakh","median")
).reset_index().round(2).to_csv(REPORTS/"real_estate_city_kpis.csv", index=False)

customers.groupby("Acquisition_Channel").agg(
    customers=("Customer_ID","count"), revenue=("Total_Revenue","sum"),
    avg_revenue=("Total_Revenue","mean"),
    churn_rate_pct=("Churned",lambda s:s.mean()*100)
).reset_index().round(2).to_csv(REPORTS/"customer_channel_kpis.csv", index=False)

products.groupby("Category").agg(
    products=("Product_ID","count"), stock_units=("Stock_Units","sum"),
    avg_monthly_sales=("Avg_Monthly_Sales","sum"),
    avg_gross_margin_pct=("gross_margin_pct","mean")
).reset_index().round(2).to_csv(REPORTS/"product_category_kpis.csv", index=False)

print("Dashboard supporting KPI tables regenerated.")
print("Open dashboard_v1.html in a browser to view the interactive dashboard.")
