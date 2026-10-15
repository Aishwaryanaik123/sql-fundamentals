"""Interactive Dash dashboard for the demo placement dataset."""
from pathlib import Path
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "student_placement_data.csv")
df["placement_status"] = df["placed"].map({1: "Placed", 0: "Not placed"})

app = Dash(__name__)
branches = sorted(df["branch"].unique())

app.layout = html.Div(
    [
        html.H1("Student Placement Analytics"),
        html.P("Interactive demo dashboard — sample data only."),
        html.Label("Filter by branch"),
        dcc.Dropdown(
            id="branch-filter",
            options=[{"label": "All branches", "value": "ALL"}]
                    + [{"label": b, "value": b} for b in branches],
            value="ALL", clearable=False
        ),
        dcc.Graph(id="salary-chart"),
        dcc.Graph(id="placement-chart"),
    ],
    style={"maxWidth": "1100px", "margin": "30px auto", "fontFamily": "Arial"}
)

@app.callback(
    Output("salary-chart", "figure"),
    Output("placement-chart", "figure"),
    Input("branch-filter", "value"),
)
def update_charts(selected_branch):
    filtered = df if selected_branch == "ALL" else df[df["branch"] == selected_branch]
    salary = px.bar(
        filtered.groupby("branch", as_index=False)["salary_lpa"].mean(),
        x="branch", y="salary_lpa", title="Average Salary by Branch",
        labels={"branch": "Branch", "salary_lpa": "Average salary (LPA)"}
    )
    placement_counts = filtered["placement_status"].value_counts().rename_axis(
        "placement_status"
    ).reset_index(name="count")
    placement = px.pie(
        placement_counts, names="placement_status", values="count",
        title="Placement Status Distribution", hole=0.35
    )
    return salary, placement

if __name__ == "__main__":
    app.run(debug=False)
