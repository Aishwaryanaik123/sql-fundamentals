"""Create interactive Plotly HTML charts from the demo placement dataset."""
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "student_placement_data.csv"
OUT = ROOT / "outputs"
REQUIRED = {
    "branch", "cgpa", "aptitude_score", "technical_score",
    "communication_score", "salary_lpa", "placed"
}

def main():
    OUT.mkdir(exist_ok=True)
    df = pd.read_csv(DATA)
    missing = REQUIRED.difference(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")
    if df.empty:
        raise ValueError("Dataset contains no rows.")

    df["placement_status"] = df["placed"].map({1: "Placed", 0: "Not placed"})
    df["cgpa_band"] = pd.cut(
        df["cgpa"], bins=[0, 6.5, 7.0, 7.5, 8.0, 10],
        labels=["≤6.5", "6.51–7.0", "7.01–7.5", "7.51–8.0", ">8.0"],
        include_lowest=True
    )

    charts = {
        "average_salary_by_branch.html": px.bar(
            df.groupby("branch", as_index=False)["salary_lpa"].mean()
              .sort_values("salary_lpa", ascending=False),
            x="branch", y="salary_lpa", title="Average Salary by Branch",
            labels={"branch": "Branch", "salary_lpa": "Average salary (LPA)"},
            hover_data={"salary_lpa": ":.2f"}
        ),
        "cgpa_vs_salary.html": px.scatter(
            df, x="cgpa", y="salary_lpa", color="placement_status",
            hover_data=["branch", "technical_score", "communication_score"],
            title="CGPA vs Salary by Placement Status",
            labels={"cgpa": "CGPA", "salary_lpa": "Salary (LPA)"}
        ),
        "placement_distribution.html": px.pie(
            df, names="placement_status", title="Placement Status Distribution",
            hole=0.35
        ),
        "salary_by_cgpa_band.html": px.line(
            df.groupby("cgpa_band", observed=False, as_index=False)["salary_lpa"].mean(),
            x="cgpa_band", y="salary_lpa", markers=True,
            title="Average Salary by CGPA Band",
            labels={"cgpa_band": "CGPA band", "salary_lpa": "Average salary (LPA)"}
        ),
    }

    # Graph Objects provides more direct control over traces and layout.
    scores = df.groupby("branch", as_index=False)[
        ["technical_score", "communication_score"]
    ].mean()
    fig_go = go.Figure()
    fig_go.add_trace(go.Bar(
        x=scores["branch"], y=scores["technical_score"],
        name="Technical score", hovertemplate="%{x}<br>Technical: %{y:.2f}<extra></extra>"
    ))
    fig_go.add_trace(go.Bar(
        x=scores["branch"], y=scores["communication_score"],
        name="Communication score", hovertemplate="%{x}<br>Communication: %{y:.2f}<extra></extra>"
    ))
    fig_go.update_layout(
        title="Average Skill Scores by Branch",
        xaxis_title="Branch", yaxis_title="Average score",
        barmode="group", template="plotly_white"
    )
    charts["skill_scores_graph_objects.html"] = fig_go

    for filename, fig in charts.items():
        path = OUT / filename
        fig.write_html(path, include_plotlyjs=True, full_html=True)
        if not path.exists() or path.stat().st_size == 0:
            raise RuntimeError(f"Chart export failed: {path}")
        print(f"Created {path.relative_to(ROOT)} ({path.stat().st_size:,} bytes)")

    print(f"Verified {len(charts)} interactive HTML charts from {len(df)} demo rows.")

if __name__ == "__main__":
    main()
