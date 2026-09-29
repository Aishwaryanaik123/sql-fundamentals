import pandas as pd

df = pd.read_csv("student_performance.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())


from autoviz import AutoViz_Class

AV = AutoViz_Class()

print("Starting AutoViz...")

AV.AutoViz(
    filename="",
    dfte=df,
    depVar="",
    header=0,
    verbose=1,
    chart_format="html",
    max_rows_analyzed=150000,
    max_cols_analyzed=30
)

print("AutoViz analysis completed!")



import sweetviz as sv

print("Starting SweetViz...")

report = sv.analyze(df)

report.show_html("sweetviz_report.html")

print("SweetViz report generated successfully!")



print("\n--- DATA INSIGHTS ---")

# 1. Missing values
print("\nMissing values:")
print(df.isnull().sum().sort_values(ascending=False).head(5))

# 2. Placement rate
print("\nPlacement status:")
print(df["placement_status"].value_counts())
print("\nPlacement rate (%):")
print(df["placement_status"].mean() * 100)

# 3. Average scores by placement status
print("\nAverage CGPA and coding skills by placement:")
print(
    df.groupby("placement_status")[
        ["cgpa", "coding_skills", "internships"]
    ].mean().round(2)
)