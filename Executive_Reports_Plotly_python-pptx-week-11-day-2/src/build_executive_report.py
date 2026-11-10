"""Reference rebuild script. Requires plotly and python-pptx."""
from pathlib import Path
import csv
from collections import defaultdict
import plotly.graph_objects as go
from pptx import Presentation
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/"data"/"executive_sales_data.csv").open(encoding="utf-8")))
annual=defaultdict(float)
for r in rows: annual[int(r["year"])]+=float(r["sales"])
fig=go.Figure(go.Bar(x=list(annual),y=[annual[y] for y in annual]))
fig.update_layout(title="Annual Sales Performance",template="plotly_white")
(ROOT/"reports"/"annual_sales.html").write_text(fig.to_html(full_html=True,include_plotlyjs=True),encoding="utf-8")
prs=Presentation(); slide=prs.slides.add_slide(prs.slide_layouts[0])
slide.shapes.title.text="Executive Sales Report"
slide.placeholders[1].text="Generated with python-pptx; synthetic sample dataset."
prs.save(ROOT/"reports"/"regenerated_summary.pptx")
print("Generated optional summary outputs.")
