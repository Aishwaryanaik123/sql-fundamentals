# Dashboard Build and Stakeholder Sharing Guide

## 1. Start Apache Superset
Prerequisite: Docker Desktop installed and running.
1. Open PowerShell in this project folder.
2. Replace the sample `SUPERSET_SECRET_KEY` in `docker-compose.yml` with a long random secret.
3. Run `docker compose up -d`.
4. Create an administrator: `docker compose exec superset superset fab create-admin`.
5. Open `http://localhost:8088` and sign in.

## 2. Connect the data
1. Load `data/sales_performance.csv` into a supported database (for example PostgreSQL) as `sales_performance`.
2. In Superset, open **Settings → Database Connections** and add the database using its SQLAlchemy URI.
3. Go to **Data → Datasets → + Dataset** and register the `sales_performance` table.
4. Verify `order_date` is a date and sales, profit, orders are numeric.

## 3. Build the five charts
Use `sql/dashboard_queries.sql` as a query reference.
- **Bar chart:** X-axis `region`; metric `SUM(sales)`.
- **Line chart:** time column `order_date`; time grain month; metric `SUM(sales)`.
- **Pie chart:** dimension `product_category`; metric `SUM(sales)`.
- **Table:** region, total orders, total sales, total profit, profit margin.
- **Metric card(s):** total sales, total profit, total orders, average order value using Big Number visualizations.

Save each chart. Create a dashboard named **Sales Performance – Stakeholder Dashboard** and add all five chart types. Put KPI cards at the top, trend and regional charts in the middle, and product mix/table below.

## 4. Export as PNG
1. Open the saved dashboard and apply desired filters.
2. Use the dashboard menu (**…**) and choose **Export / Download as image** if supported by your Superset version.
3. Save the exported image under `dashboard/`.
4. If your version does not offer PNG export, use an approved full-page screenshot method.
5. Do not describe the included preview PNG as a native Superset export.

## 5. Share with a stakeholder
1. Confirm all charts load and totals are correct.
2. Grant the stakeholder a role with only the necessary dashboard and dataset permissions.
3. Share the dashboard URL. A `localhost` URL is accessible only on the creator's machine; use an approved hosted environment for remote stakeholders.
4. For external access, use HTTPS and organizational authentication. Do not expose a local development server directly to the public internet.
5. Send the PNG/PDF snapshot with a short explanation of date range, KPIs, and data limitations.
6. Ask for feedback on regional performance, sales trend, product mix, and follow-up questions.

## Suggested stakeholder message
Please review the Sales Performance dashboard for January 2024–December 2025. It summarizes sales, profit, order volume, monthly trends, regional contribution, and product category mix. The dataset is synthetic and intended for dashboard practice.

## Validation checklist
- [ ] Superset starts and login works
- [ ] Database connection succeeds
- [ ] Dataset registered with correct data types
- [ ] Bar, line, pie, table, and metric visualizations saved
- [ ] All five chart types appear on dashboard
- [ ] Filters and totals checked
- [ ] PNG exported from live Superset dashboard
- [ ] Stakeholder permissions and URL tested
