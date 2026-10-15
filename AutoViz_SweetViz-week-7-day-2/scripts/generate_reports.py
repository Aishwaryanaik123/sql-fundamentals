"""
Generate native AutoViz and SweetViz HTML reports from student_performance.csv.
Run from this folder after installing requirements.txt and placing the CSV beside this script
or passing its path as the first command-line argument.
"""
from pathlib import Path
import sys
import pandas as pd

csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("student_performance.csv")
if not csv_path.exists():
    raise FileNotFoundError(
        f"Dataset not found: {csv_path}. Supply the path to student_performance.csv."
    )

df = pd.read_csv(csv_path)
out_dir = Path("native_reports")
out_dir.mkdir(exist_ok=True)

# SweetViz native HTML report
import sweetviz as sv
target = "placement_status" if "placement_status" in df.columns else None
report = sv.analyze(df, target_feat=target)
report.show_html(str(out_dir / "sweetviz_report.html"), open_browser=False)

# AutoViz native output (AutoViz writes plots/reports to its configured output folder)
from autoviz import AutoViz_Class
AV = AutoViz_Class()
AV.AutoViz(
    filename=str(csv_path),
    sep=",",
    depVar=target or "",
    dfte=None,
    header=0,
    verbose=1,
    lowess=False,
    chart_format="html",
    max_rows_analyzed=100000,
    max_cols_analyzed=18,
)
print(f"SweetViz report saved in {out_dir.resolve()}")
print("Check the AutoViz output folder created by the installed AutoViz version.")
