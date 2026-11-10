# Week 12 — Final Dashboard + Strategic Brief

## Deliverables
- `final_dashboard.html` — responsive interactive Plotly dashboard.
- `reports/Strategic_Brief_Week_12.pdf` — two-page strategic brief.
- `data/dashboard_aggregate_data.json` — aggregate data embedded from the prior Week 9 dashboard.
- `reports/revision_status.md` — traceability of Week 9 revisions.
- `reports/your_work_summary.txt` — internship submission summary.
- `reports/tools_used.txt` — tools used.

## Run
Open `final_dashboard.html` in a modern browser with an internet connection (Plotly is loaded from its CDN).

## Final dashboard coverage
Executive KPI cards; city sold-rate and median-price charts; acquisition-channel revenue; churn split; category stock versus average monthly sales; category gross margin; category table; KPI glossary; revision and limitation notes.

## Data integrity
This package uses the aggregate city/channel/category arrays retained in the Week 9 dashboard source and KPI catalogue. The raw source CSVs were not available in the retrieved project files for this Week 12 build. Accordingly, it does not fabricate product-level stock-risk rows. Customer revenue remains in source units because currency is unspecified. The source refresh date was not supplied. The Week 9 peer-review file says its sample review was illustrative, so a real peer review remains to be completed and documented.

## Tools
HTML5, CSS3, JavaScript, Plotly.js, Python (ReportLab for PDF generation).
