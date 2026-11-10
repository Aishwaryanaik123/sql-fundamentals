# Week 9 — Dashboard v1 + Peer Review

# Business Analytics Dashboard v1 + Peer Review

## Objective
Publish a first dashboard version covering all available KPIs across three supplied datasets: real estate listings, customer profiles, and product catalogue. Record a heuristic review and produce a prioritized revision list.

## Deliverables
- `dashboard_v1.html` — interactive dashboard with KPI cards and charts.
- `data/` — original source CSV files.
- `reports/kpi_catalogue.csv` — KPI definitions and values.
- `reports/real_estate_city_kpis.csv` — city-level property metrics.
- `reports/customer_channel_kpis.csv` — customer metrics by acquisition channel.
- `reports/product_category_kpis.csv` — product/inventory metrics by category.
- `reports/product_stock_risk.csv` — products where stock is below average monthly sales.
- `reports/peer_heuristic_review_log.md` — review log and actual peer-feedback capture section.
- `reports/revision_list.md` — prioritized changes for dashboard v2.
- `reports/Dashboard_V1_Review_Report.pdf` — submission report.
- `src/build_dashboard.py` — reproducible dashboard build script.

## How to view
Open `dashboard_v1.html` in a modern browser. An internet connection is required to load the Plotly JavaScript library from its CDN.

## Key KPI snapshot
- Real estate: 600 listings, 209 sold, 34.83% sold rate, median price 172.595 lakh, average days on market 183.7.
- Customers: 200 customers, 4,992,621 revenue source units, 2,307 orders, 6 churned, 3.00% churn rate.
- Products: 50 products, 13,857 stock units, 5,276 average monthly sales units, 58.62% average gross margin, 5 stock-risk products.

## Data and methodology notes
The three datasets have different grains and no confirmed shared join key. They are intentionally shown as separate business domains. Revenue currency/unit is not specified; values are reported in source units. Average gross margin is the unweighted mean of product-level margins `(MRP - COGS) / MRP`. The dashboard is descriptive and does not claim causality or prediction.

## Peer-review integrity note
The included review log contains an explicitly labelled illustrative/simulated heuristic review and a blank section for actual peer feedback. It must not be represented as a completed real peer review. To complete the requirement, share the HTML dashboard with one peer, record their name/date/comments, and replace the sample notes with their actual feedback.
