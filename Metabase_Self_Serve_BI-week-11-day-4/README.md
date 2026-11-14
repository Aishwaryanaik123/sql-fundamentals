# Week 11 Day 4 – Metabase Self-Serve BI Setup

## Learning objective
Prepare a self-service Business Intelligence dashboard using Metabase, a synthetic sales dataset, and five common visualization types.

## Project contents
- `data/sales_performance.csv` – 288 synthetic records for January 2024–December 2025.
- `data/sales_performance.sqlite` – ready-to-open SQLite copy of the dataset.
- `dashboard/metabase_dashboard_preview.png` – combined dashboard preview.
- `dashboard/` – individual previews for bar, line, pie, table, and KPI cards.
- `sql/metabase_questions.sql` – SQL examples for the dashboard questions.
- `docker-compose.yml` – local Metabase and PostgreSQL reference setup.
- `docs/metabase_setup_and_sharing_guide.md` – setup, database connection, dashboard creation, export, and stakeholder sharing.

## Sample KPI results
- Total sales: $4,624,904.41
- Total profit: $838,700.25
- Total orders: 12,556
- Average order value: $368.34

## Start Metabase locally
Docker Desktop must be installed and running. Review `docker-compose.yml` and change the sample credentials before use outside a disposable local environment. From this project directory, run:

`docker compose up -d`

Open `http://localhost:3000` and complete the first-time Metabase setup. The Compose file creates a PostgreSQL service for the Metabase application metadata. Add your sales data as a separate Metabase data source, following the guide.

## Important execution note
Metabase was not launched in this build environment. The included PNG is a locally generated dashboard preview, not an image exported from a running Metabase instance. Follow the guide to connect the included SQLite file or import the CSV into PostgreSQL, create the five visualizations, and export a live dashboard image if your instructor requires a native Metabase export.

All sales records are synthetic and intended for training only.
