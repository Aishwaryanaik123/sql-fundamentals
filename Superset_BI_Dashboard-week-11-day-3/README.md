# Week 11 Day 3 – Apache Superset BI Dashboard

## Objective
Prepare a stakeholder-focused BI dashboard specification with five requested chart types: bar, line, pie, table, and KPI metric cards.

## Included deliverables
- `data/sales_performance.csv` – 288 synthetic records from Jan 2024 to Dec 2025.
- `dashboard/sales_stakeholder_dashboard_preview.png` – combined dashboard preview.
- `dashboard/` – individual previews for bar, line, pie, table, and metric cards.
- `sql/dashboard_queries.sql` – SQL queries for each visualization.
- `docker-compose.yml` and `superset/superset_config.py` – local Superset setup reference.
- `docs/dashboard_build_and_sharing_guide.md` – setup, chart creation, PNG export, and stakeholder sharing steps.

## Sample KPI results
- Total sales: $4,570,018.75
- Total profit: $818,525.49
- Total orders: 12,973
- Average order value: $352.27

## Run locally
Docker Desktop is required and must be running. Review the Compose file and replace its placeholder secret. Then run `docker compose up -d` from this folder. Create an administrator account with `docker compose exec superset superset fab create-admin`, then open `http://localhost:8088`.

**Execution note:** Apache Superset was not launched in this build environment. The included PNG is a locally generated dashboard preview, not a screenshot exported from a live Superset instance. Follow the guide to create the live dashboard and export it from Superset if your instructor requires a native export. All sample sales data is synthetic.
