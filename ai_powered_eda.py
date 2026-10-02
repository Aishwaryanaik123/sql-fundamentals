# ============================================================
# W5D5 - AI-Powered EDA on Indian Business/Student Dataset
# ============================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. Load Dataset
# ============================================================

file_path = "student_performance.csv"

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found.")
    print("Make sure the CSV file is in the same folder as this Python file.")
    exit()

df = pd.read_csv(file_path)

print("=" * 60)
print("AI-POWERED EXPLORATORY DATA ANALYSIS")
print("=" * 60)

print("\nDataset loaded successfully.")


# ============================================================
# 2. Dataset Overview
# ============================================================

print("\n" + "=" * 60)
print("1. DATASET OVERVIEW")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)


# ============================================================
# 3. Dataset Information
# ============================================================

print("\n" + "=" * 60)
print("2. DATASET INFORMATION")
print("=" * 60)

print(df.info())


# ============================================================
# 4. Missing Value Analysis
# ============================================================

print("\n" + "=" * 60)
print("3. MISSING VALUE ANALYSIS")
print("=" * 60)

missing_values = df.isnull().sum()

print("\nMissing Values:")
print(missing_values)

missing_percentage = (df.isnull().sum() / len(df)) * 100

missing_summary = pd.DataFrame({
    "Missing Values": missing_values,
    "Missing Percentage": missing_percentage
})

print("\nMissing Value Summary:")
print(missing_summary)


# ============================================================
# 5. Duplicate Analysis
# ============================================================

print("\n" + "=" * 60)
print("4. DUPLICATE ANALYSIS")
print("=" * 60)

duplicate_count = df.duplicated().sum()

print(f"\nNumber of duplicate rows: {duplicate_count}")


# ============================================================
# 6. Descriptive Statistics
# ============================================================

print("\n" + "=" * 60)
print("5. DESCRIPTIVE STATISTICS")
print("=" * 60)

print("\nNumerical Statistics:")
print(df.describe())

print("\nCategorical Statistics:")
print(df.describe(include=["str"]))


# ============================================================
# 7. Numerical and Categorical Columns
# ============================================================

print("\n" + "=" * 60)
print("6. COLUMN TYPES")
print("=" * 60)

numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
categorical_columns = df.select_dtypes(include=["str"]).columns.tolist()

print("\nNumerical Columns:")
print(numeric_columns)

print("\nCategorical Columns:")
print(categorical_columns)


# ============================================================
# 8. Categorical Analysis
# ============================================================

print("\n" + "=" * 60)
print("7. CATEGORICAL ANALYSIS")
print("=" * 60)

for column in categorical_columns:
    print(f"\n--- {column} ---")
    print(df[column].value_counts().head(10))


# ============================================================
# 9. Correlation Analysis
# ============================================================

print("\n" + "=" * 60)
print("8. CORRELATION ANALYSIS")
print("=" * 60)

correlation_matrix = df[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix.round(2))


# ============================================================
# 10. Create Output Folder
# ============================================================

output_folder = "eda_outputs"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print(f"\nEDA output folder created: {output_folder}")


# ============================================================
# 11. Correlation Heatmap
# ============================================================

plt.figure(figsize=(12, 9))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "correlation_heatmap.png"),
    dpi=300
)

plt.show()


# ============================================================
# 12. CGPA Distribution
# ============================================================

if "cgpa" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.histplot(
        df["cgpa"],
        kde=True
    )

    plt.title("CGPA Distribution")
    plt.xlabel("CGPA")
    plt.ylabel("Number of Students")

    plt.tight_layout()

    plt.savefig(
        os.path.join(output_folder, "cgpa_distribution.png"),
        dpi=300
    )

    plt.show()


# ============================================================
# 13. Placement Status Analysis
# ============================================================

if "placement_status" in df.columns:

    print("\n" + "=" * 60)
    print("9. PLACEMENT STATUS ANALYSIS")
    print("=" * 60)

    placement_counts = df["placement_status"].value_counts()

    print("\nPlacement Status:")
    print(placement_counts)

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="placement_status"
    )

    plt.title("Placement Status Distribution")
    plt.xlabel("Placement Status")
    plt.ylabel("Number of Students")

    plt.tight_layout()

    plt.savefig(
        os.path.join(output_folder, "placement_status.png"),
        dpi=300
    )

    plt.show()


# ============================================================
# 14. Salary Package Analysis
# ============================================================

if "salary_package_lpa" in df.columns:

    print("\n" + "=" * 60)
    print("10. SALARY PACKAGE ANALYSIS")
    print("=" * 60)

    print("\nSalary Statistics:")
    print(df["salary_package_lpa"].describe())

    plt.figure(figsize=(8, 5))

    sns.histplot(
        df["salary_package_lpa"],
        kde=True
    )

    plt.title("Salary Package Distribution")
    plt.xlabel("Salary Package (LPA)")
    plt.ylabel("Number of Students")

    plt.tight_layout()

    plt.savefig(
        os.path.join(output_folder, "salary_distribution.png"),
        dpi=300
    )

    plt.show()


# ============================================================
# 15. CGPA vs Salary
# ============================================================

if "cgpa" in df.columns and "salary_package_lpa" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="cgpa",
        y="salary_package_lpa"
    )

    plt.title("CGPA vs Salary Package")
    plt.xlabel("CGPA")
    plt.ylabel("Salary Package (LPA)")

    plt.tight_layout()

    plt.savefig(
        os.path.join(output_folder, "cgpa_vs_salary.png"),
        dpi=300
    )

    plt.show()


# ============================================================
# 16. Coding Skills vs Placement
# ============================================================

if "coding_skills" in df.columns and "placement_status" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x="placement_status",
        y="coding_skills"
    )

    plt.title("Coding Skills vs Placement Status")
    plt.xlabel("Placement Status")
    plt.ylabel("Coding Skills")

    plt.tight_layout()

    plt.savefig(
        os.path.join(output_folder, "coding_skills_vs_placement.png"),
        dpi=300
    )

    plt.show()


# ============================================================
# 17. DSA Score vs Placement
# ============================================================

if "dsa_score" in df.columns and "placement_status" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x="placement_status",
        y="dsa_score"
    )

    plt.title("DSA Score vs Placement Status")
    plt.xlabel("Placement Status")
    plt.ylabel("DSA Score")

    plt.tight_layout()

    plt.savefig(
        os.path.join(output_folder, "dsa_vs_placement.png"),
        dpi=300
    )

    plt.show()


# ============================================================
# 18. Internship vs Placement
# ============================================================

if "internships" in df.columns and "placement_status" in df.columns:

    placement_by_internship = pd.crosstab(
        df["internships"],
        df["placement_status"]
    )

    print("\n" + "=" * 60)
    print("11. INTERNSHIPS VS PLACEMENT")
    print("=" * 60)

    print(placement_by_internship)


# ============================================================
# 19. Top Correlations
# ============================================================

print("\n" + "=" * 60)
print("12. TOP CORRELATIONS")
print("=" * 60)

correlation_pairs = correlation_matrix.where(
    np.triu(
        np.ones(correlation_matrix.shape),
        k=1
    ).astype(bool)
)

top_correlations = (
    correlation_pairs
    .stack()
    .sort_values(
        key=lambda x: abs(x),
        ascending=False
    )
)

print("\nStrongest relationships:")
print(top_correlations.head(10))


# ============================================================
# 20. AI-Style Business Insights
# ============================================================

print("\n" + "=" * 60)
print("13. DATA-DRIVEN BUSINESS INSIGHTS")
print("=" * 60)

if "cgpa" in df.columns:
    print(
        f"\n• Average CGPA: "
        f"{df['cgpa'].mean():.2f}"
    )

if "salary_package_lpa" in df.columns:
    print(
        f"• Average Salary Package: "
        f"{df['salary_package_lpa'].mean():.2f} LPA"
    )

if "placement_status" in df.columns:

    placement_rate = (
        df["placement_status"]
        .value_counts(normalize=True)
        * 100
    )

    print("\n• Placement Status Percentage:")
    print(placement_rate.round(2))

if "internships" in df.columns:

    print(
        "\n• Internship Statistics:"
    )

    print(
        df["internships"].describe()
    )

if "coding_skills" in df.columns:

    print(
        f"\n• Average Coding Skills Score: "
        f"{df['coding_skills'].mean():.2f}"
    )

if "dsa_score" in df.columns:

    print(
        f"• Average DSA Score: "
        f"{df['dsa_score'].mean():.2f}"
    )

if "communication_skills" in df.columns:

    print(
        f"• Average Communication Skills Score: "
        f"{df['communication_skills'].mean():.2f}"
    )


# ============================================================
# 21. Save EDA Summary
# ============================================================

summary_file = os.path.join(
    output_folder,
    "eda_summary.txt"
)

with open(summary_file, "w", encoding="utf-8") as file:

    file.write("AI-POWERED EDA SUMMARY\n")
    file.write("=" * 50 + "\n\n")

    file.write(f"Dataset Shape: {df.shape}\n\n")

    file.write(
        f"Duplicate Rows: {duplicate_count}\n\n"
    )

    file.write(
        "Missing Values:\n"
    )

    file.write(
        missing_values.to_string()
    )

    file.write("\n\n")

    file.write(
        "Descriptive Statistics:\n"
    )

    file.write(
        df.describe().to_string()
    )

    file.write("\n\n")

    file.write(
        "Correlation Matrix:\n"
    )

    file.write(
        correlation_matrix.round(2).to_string()
    )


# ============================================================
# 22. Final Message
# ============================================================

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated files are available inside:")

print("eda_outputs/")

print("\nGenerated outputs include:")
print("- correlation_heatmap.png")
print("- cgpa_distribution.png")
print("- placement_status.png")
print("- salary_distribution.png")
print("- cgpa_vs_salary.png")
print("- coding_skills_vs_placement.png")
print("- dsa_vs_placement.png")
print("- eda_summary.txt")

print("\nAll analysis completed successfully.")