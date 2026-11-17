"""Load 100k CSV rows into DuckDB and execute five analytical queries."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from duckdb_utils import query_to_df, close_connection

queries = {
    "q1_overall_kpis": "SELECT COUNT(*) AS order_lines, ROUND(SUM(sales),2) AS total_sales, ROUND(SUM(profit),2) AS total_profit, ROUND(AVG(sales),2) AS avg_line_sales FROM sales",
    "q2_region_performance": "SELECT region, ROUND(SUM(sales),2) AS total_sales, ROUND(SUM(profit),2) AS total_profit FROM sales GROUP BY region ORDER BY total_sales DESC",
    "q3_category_performance": "SELECT category, COUNT(*) AS order_lines, ROUND(SUM(sales),2) AS total_sales, ROUND(SUM(profit),2) AS total_profit FROM sales GROUP BY category ORDER BY total_sales DESC",
    "q4_monthly_trend": "SELECT DATE_TRUNC('month', CAST(order_date AS DATE)) AS sales_month, ROUND(SUM(sales),2) AS monthly_sales FROM sales GROUP BY 1 ORDER BY 1",
    "q5_customer_segment": "SELECT customer_segment, COUNT(*) AS order_lines, ROUND(SUM(sales),2) AS total_sales, ROUND(AVG(discount_pct)*100,2) AS avg_discount_percent FROM sales GROUP BY customer_segment ORDER BY total_sales DESC",
}
report_dir = ROOT / "reports"; report_dir.mkdir(exist_ok=True)
for name, sql in queries.items():
    df = query_to_df(sql)
    df.to_csv(report_dir / f"{name}.csv", index=False)
    print(f"\n{name}\n{df.to_string(index=False)}")
print("\nCompleted five DuckDB analytical queries. Results saved in reports/.")
close_connection()
