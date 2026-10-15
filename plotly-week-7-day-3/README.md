# Plotly Interactive Visualization — Week 7 Day 3

## Objective
Use Plotly Express and Plotly Graph Objects to create interactive charts, export them as HTML, and provide a small Plotly Dash analytics app.

## Important data note
`data/student_placement_data.csv` is a small **sample/demo dataset created for this practical**, not real student or company data. Replace it with an approved assignment dataset if one was supplied separately.

## Project contents
- `data/student_placement_data.csv` — sample placement dataset.
- `src/create_charts.py` — creates interactive HTML charts using Plotly Express and Graph Objects.
- `src/dash_app.py` — interactive Dash web dashboard with a branch filter.
- `outputs/` — HTML charts generated from the sample dataset (when generated in an environment with the listed dependencies).
- `docs/insights.md` — example insights from the demo data.
- `WORKLOG.md` — task summary.
- `TOOLS_USED.txt` — tools and libraries.
- `requirements.txt` — Python dependencies.

## Charts included
1. Bar chart — average salary by branch.
2. Scatter plot — CGPA vs salary, colored by placement status.
3. Pie chart — placement status distribution.
4. Line chart — average salary by CGPA band.
5. Graph Objects chart — average technical and communication scores by branch.

## Run instructions
Python 3.10+ is recommended.

```bash
python -m pip install -r requirements.txt
python src/create_charts.py
python src/dash_app.py
```

The chart script saves self-contained HTML files in `outputs/`. The Dash app runs locally and prints its URL in the terminal.

## Verification
The chart generation script validates required columns, creates each chart, writes the HTML output, and checks that the output files exist. The data is synthetic/demo data, so describe findings as illustrative rather than factual.
