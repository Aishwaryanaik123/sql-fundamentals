# Metabase Setup and Stakeholder Sharing Guide

## 1. Start Metabase locally
Prerequisite: Docker Desktop installed and running.
1. Open PowerShell in this project folder.
2. Review `docker-compose.yml` and replace sample credentials if needed.
3. Run `docker compose up -d`.
4. Open `http://localhost:3000`.
5. Complete the first-time setup wizard and create your administrator account.

## 2. Connect the sales data
Two prepared data options are included:
- `data/sales_performance.sqlite` – ready-to-use SQLite database file.
- `data/sales_performance.csv` – CSV for importing into PostgreSQL or another supported database.

In Metabase:
1. Open **Admin settings → Databases → Add database**.
2. Select SQLite and enter the path to the mounted/shared SQLite file if your Metabase deployment can access it. For Docker, copy or mount the SQLite file into the container and use its container path.
3. Alternatively, import the CSV into a PostgreSQL database and connect using the host, port, database, username, and password for that data source.
4. Confirm `order_date` is recognized as a date and `sales`, `profit`, and `orders` are numeric.
5. Sync the database schema if needed.

## 3. Create the five required visualizations
Use the query examples in `sql/metabase_questions.sql`, or use Metabase's query builder.

| Required visualization | Metabase chart type | Suggested fields |
|---|---|---|
| Bar | Bar | Region; Sum of sales |
| Line | Line | Order date by month; Sum of sales |
| Pie | Pie | Product category; Sum of sales |
| Table | Table | Region, orders, sales, profit, profit margin |
| Metric card | Number | Sum of sales, sum of profit, sum of orders, average order value |

Save each question with a clear name. For KPI metric cards, save separate Number questions for Total Sales, Total Profit, Total Orders, and Average Order Value.

## 4. Build and export the dashboard
1. Select **New → Dashboard** and name it **Sales Performance – Self-Serve BI**.
2. Add the five chart types and the saved KPI questions.
3. Arrange KPI cards at the top, regional and monthly charts in the middle, and category mix/table below.
4. Add a date filter if useful and connect it to the relevant cards.
5. Save the dashboard and verify that every card loads.
6. Use the dashboard menu to choose **Export** or the available image/screenshot option for your Metabase version. If native PNG export is unavailable, use an approved browser full-page screenshot workflow.
7. Save the verified live export in the `dashboard/` folder. Do not label the supplied preview as a live export.

## 5. Share with a stakeholder
1. Confirm the dashboard and filters work.
2. Grant the stakeholder access using a Metabase collection and group with only the required permissions.
3. Share the dashboard link from the same network or approved hosted environment. `localhost` works only on the creator's machine.
4. For remote stakeholders, deploy Metabase behind HTTPS and organizational authentication; do not expose a local development server publicly.
5. Share a PNG/PDF snapshot with a short explanation of the reporting period, KPIs, and data limitations.
6. Ask the stakeholder to review regional sales, monthly trends, product mix, and any follow-up questions.

## Suggested stakeholder handoff message
Please review the Sales Performance dashboard for January 2024–December 2025. It summarizes sales, profit, order volume, monthly trends, regional contribution, and product category mix. The dataset is synthetic and intended for dashboard practice.

## Validation checklist
- [ ] Metabase starts and first-time setup completes.
- [ ] Sales database is connected.
- [ ] Date and numeric fields have correct data types.
- [ ] Bar, line, pie, table, and metric visualizations are saved.
- [ ] All visualizations appear on the dashboard.
- [ ] Filters and totals are checked.
- [ ] Live dashboard image is exported.
- [ ] Stakeholder permissions and sharing URL are tested.
