from pathlib import Path
import sqlite3
import logging
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"
LOGS = ROOT / "logs"
DB_PATH = ROOT / "data" / "processed" / "analytics.db"

logging.basicConfig(
    filename=LOGS / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
FILES = {
    "real_estate": "da_realestate_listings.csv",
    "customers": "da_customer_profiles.csv",
    "products": "da_product_catalogue.csv",
}

def load_and_clean():
    frames = {}
    for table, filename in FILES.items():
        df = pd.read_csv(RAW / filename)
        df.columns = [c.strip() for c in df.columns]
        for col in df.select_dtypes(include="object").columns:
            df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)
        if table == "real_estate":
            df["listed_date"] = pd.to_datetime(df["listed_date"], errors="coerce")
        elif table == "customers":
            for col in ["First_Purchase_Date", "Last_Purchase_Date"]:
                df[col] = pd.to_datetime(df[col], errors="coerce")
        # Keep source records; fail fast on missing/duplicate candidate keys.
        key = {"real_estate":"listing_id", "customers":"Customer_ID", "products":"Product_ID"}[table]
        if df[key].isna().any() or df[key].duplicated().any():
            raise ValueError(f"{table}: candidate key {key} is missing or duplicated")
        frames[table] = df
        df.to_csv(PROCESSED / filename, index=False)
        logging.info("%s loaded: %s rows, %s columns", table, len(df), len(df.columns))
    return frames

def write_quality_report(frames):
    rows=[]
    for table, df in frames.items():
        key={"real_estate":"listing_id","customers":"Customer_ID","products":"Product_ID"}[table]
        rows.append({
            "table":table, "rows":len(df), "columns":len(df.columns),
            "missing_cells":int(df.isna().sum().sum()),
            "duplicate_rows":int(df.duplicated().sum()),
            "duplicate_key_values":int(df[key].duplicated().sum()),
            "candidate_key":key
        })
    pd.DataFrame(rows).to_csv(REPORTS / "pipeline_quality_checks.csv", index=False)

def run_sql_metrics():
    conn=sqlite3.connect(DB_PATH)
    try:
        for table, filename in FILES.items():
            df=pd.read_csv(PROCESSED / filename)
            df.to_sql(table, conn, if_exists="replace", index=False)
        query=(ROOT / "sql" / "baseline_metrics.sql").read_text(encoding="utf-8")
        metrics=pd.read_sql_query(query, conn)
        metrics.to_csv(REPORTS / "baseline_metrics.csv", index=False)

        re=pd.read_sql_query("""
            SELECT city, COUNT(*) AS listings,
                   SUM(CASE WHEN sold=1 THEN 1 ELSE 0 END) AS sold_listings,
                   ROUND(100.0*SUM(CASE WHEN sold=1 THEN 1 ELSE 0 END)/COUNT(*),2) AS sold_rate_pct,
                   ROUND(AVG(total_price_lakh),2) AS avg_price_lakh,
                   ROUND(AVG(days_on_market),2) AS avg_days_on_market
            FROM real_estate GROUP BY city ORDER BY listings DESC
        """, conn)
        re.to_csv(REPORTS / "real_estate_city_metrics.csv", index=False)

        cust=pd.read_sql_query("""
            SELECT Acquisition_Channel AS acquisition_channel,
                   COUNT(*) AS customers,
                   ROUND(SUM(Total_Revenue),2) AS total_revenue,
                   ROUND(AVG(Total_Revenue),2) AS avg_revenue_per_customer,
                   ROUND(100.0*SUM(CASE WHEN Churned=1 THEN 1 ELSE 0 END)/COUNT(*),2) AS churn_rate_pct
            FROM customers GROUP BY Acquisition_Channel ORDER BY total_revenue DESC
        """, conn)
        cust.to_csv(REPORTS / "customer_channel_metrics.csv", index=False)

        prod=pd.read_sql_query("""
            SELECT Category AS category, COUNT(*) AS products,
                   SUM(Stock_Units) AS stock_units,
                   ROUND(AVG(100.0*(MRP-COGS)/NULLIF(MRP,0)),2) AS avg_gross_margin_pct,
                   SUM(CASE WHEN Stock_Units < Avg_Monthly_Sales THEN 1 ELSE 0 END) AS low_stock_products
            FROM products GROUP BY Category ORDER BY products DESC
        """, conn)
        prod.to_csv(REPORTS / "product_category_metrics.csv", index=False)
    finally:
        conn.close()

def main():
    for folder in [PROCESSED, REPORTS, LOGS]:
        folder.mkdir(parents=True, exist_ok=True)
    logging.info("Pipeline started")
    frames=load_and_clean()
    write_quality_report(frames)
    run_sql_metrics()
    logging.info("Pipeline completed successfully")
    print("Pipeline completed. Outputs saved under reports/ and data/processed/.")

if __name__ == "__main__":
    main()
