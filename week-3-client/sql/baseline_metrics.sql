-- Week 3 baseline metrics. Tables are loaded by src/run_pipeline.py.
-- Real estate: portfolio and city-level performance
SELECT 'real_estate_overall' AS metric_group,
       'total_listings' AS metric_name, COUNT(*) AS metric_value
FROM real_estate
UNION ALL
SELECT 'real_estate_overall','sold_listings',SUM(CASE WHEN sold=1 THEN 1 ELSE 0 END) FROM real_estate
UNION ALL
SELECT 'real_estate_overall','sold_rate_pct',
       ROUND(100.0*SUM(CASE WHEN sold=1 THEN 1 ELSE 0 END)/NULLIF(COUNT(*),0),2) FROM real_estate
UNION ALL
SELECT 'real_estate_overall','median_price_lakh',
       (SELECT AVG(x) FROM (SELECT total_price_lakh AS x FROM real_estate ORDER BY x LIMIT 2 - (SELECT COUNT(*) FROM real_estate)%2 OFFSET (SELECT (COUNT(*)-1)/2 FROM real_estate)))
UNION ALL
SELECT 'real_estate_overall','avg_days_on_market',ROUND(AVG(days_on_market),2) FROM real_estate
UNION ALL
SELECT 'customer_overall','total_customers',COUNT(*) FROM customers
UNION ALL
SELECT 'customer_overall','churned_customers',SUM(CASE WHEN Churned=1 THEN 1 ELSE 0 END) FROM customers
UNION ALL
SELECT 'customer_overall','churn_rate_pct',ROUND(100.0*SUM(CASE WHEN Churned=1 THEN 1 ELSE 0 END)/NULLIF(COUNT(*),0),2) FROM customers
UNION ALL
SELECT 'customer_overall','total_revenue',ROUND(SUM(Total_Revenue),2) FROM customers
UNION ALL
SELECT 'customer_overall','avg_revenue_per_customer',ROUND(AVG(Total_Revenue),2) FROM customers
UNION ALL
SELECT 'customer_overall','avg_orders_per_customer',ROUND(AVG(Total_Orders),2) FROM customers
UNION ALL
SELECT 'product_overall','total_products',COUNT(*) FROM products
UNION ALL
SELECT 'product_overall','total_stock_units',SUM(Stock_Units) FROM products
UNION ALL
SELECT 'product_overall','products_below_monthly_sales',
       SUM(CASE WHEN Stock_Units < Avg_Monthly_Sales THEN 1 ELSE 0 END) FROM products
UNION ALL
SELECT 'product_overall','avg_gross_margin_pct',
       ROUND(AVG(100.0*(MRP-COGS)/NULLIF(MRP,0)),2) FROM products;

-- Supporting segment metrics are generated separately by Python group-bys for easy CSV export.
