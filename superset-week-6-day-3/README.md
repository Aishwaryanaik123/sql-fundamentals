# Apache Superset Dashboard – Practical Task Submission

## Practical Tasks Covered

1. Apache Superset local setup reference with Docker configuration.
2. Dashboard containing 5 requested visualization types:
   - Bar chart
   - Line chart
   - Pie chart
   - Metric/KPI
   - Table
3. Dashboard presentation/feedback simulation and one improvement.

## Dataset

`student_placement_data.csv` contains 1,000 student placement records.

`student_placement.db` contains the same data in SQLite format in the table:
`student_placement`

## Dashboard

`dashboard_export.png` is the final dashboard export image.

Individual visualizations are available in the `charts` folder.

## Dashboard Story

The dashboard analyzes:
- Placement rate
- Average salary by branch
- Monthly salary trend
- Placement status distribution
- College-tier performance

## Feedback and Improvement

Feedback received:
"The dashboard is useful, but the most important KPI should be easier to identify immediately."

Improvement made:
- Added a prominent Overall Placement Rate KPI.
- Added an additional Average Salary KPI.
- Kept the supporting charts and table below the KPIs for faster interpretation.

## Important Note

This package is prepared as a submission-ready artifact. It does not claim that a live Apache Superset server was actually started in this environment. The Docker and Superset configuration files are included as supporting setup/reference files.
