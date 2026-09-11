import pandas as pd
import numpy as np


# 1. Load Dataset
df = pd.read_csv("Employee.csv")

print("Original Dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


# 2. Identify and Quantify Missing Values
print("\nMissing Values:")
print(df.isnull().sum())


# 3. Apply Imputation Strategies

# Numerical columns
numeric_columns = df.select_dtypes(include=np.number).columns

# Mean imputation
for column in numeric_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mean())

# Median imputation
for column in numeric_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].median())

# Categorical columns
categorical_columns = df.select_dtypes(include="str").columns

# Mode imputation
for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mode()[0])

# Forward-fill remaining missing values
df = df.ffill()

print("\nMissing Values After Imputation:")
print(df.isnull().sum())


# 4. Detect and Handle Outliers Using IQR
# IQR is applied only to appropriate continuous numerical columns
outlier_columns = ["Age", "ExperienceInCurrentDomain"]

for column in outlier_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = (
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ).sum()

    print(f"\nOutliers in {column}: {outliers}")

    # Cap outliers instead of deleting rows
    df[column] = df[column].clip(
        lower=lower_limit,
        upper=upper_limit
    )


# 5. Standardise Inconsistent String Values
for column in categorical_columns:

    # Remove extra spaces
    df[column] = df[column].astype(str).str.strip()

    # Standardise casing
    df[column] = df[column].str.title()


# Standardise common variations
for column in categorical_columns:

    df[column] = df[column].replace({
        "M": "Male",
        "F": "Female",
        "Male": "Male",
        "Female": "Female"
    })


# 6. Create Data Quality Log
quality_log = pd.DataFrame({
    "Cleaning Step": [
        "Missing value identification",
        "Mean/Median imputation",
        "Mode imputation",
        "Forward-fill",
        "IQR outlier handling",
        "String standardisation"
    ],

    "Action Taken": [
        "Checked missing values using isnull().sum()",
        "Filled numerical missing values using mean and median",
        "Filled categorical missing values using mode",
        "Forward-filled remaining missing values",
        "Capped continuous numerical outliers using IQR limits",
        "Removed whitespace and standardised text casing"
    ]
})

quality_log.to_csv("data_quality_log.csv", index=False)


# 7. Save Cleaned Dataset
df.to_csv("cleaned_employee.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as: cleaned_employee.csv")
print("Data quality log saved as: data_quality_log.csv")