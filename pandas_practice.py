''''# 1. Load a CSV into a Pandas DataFrame
import pandas as pd
df = pd.read_csv("employees.csv")
print(df)




# 2. Inspect with .head(), .info(), .describe(), .value_counts()
import pandas as pd
df = pd.read_csv("employees.csv")

# View first 5 rows
print(df.head())

# Get information about columns and data types
print(df.info())

# Get statistical summary
print(df.describe())

# Count unique values in a column
print(df["Department"].value_counts())




# 3. Filter rows, select columns, handle missing values
import pandas as pd
df = pd.read_csv("employees.csv")

# 1. Filter Rows
# Employees with salary greater than 50000
filtered_df = df[df["Salary"] > 50000]
print(filtered_df)

# 2.Select Columns
# To select a single column:
print(df["Name"])

#To select multiple columns:
print(df[["Name", "Salary"]])

# 3.Handle Missing Values
# Check for missing values:
print(df.isnull().sum())

# Remove rows with missing values:
df = df.dropna()

# Fill missing values:
df["Salary"] = df["Salary"].fillna(0)



# 4. Group by a column and aggregate
# Average salary by department
import pandas as pd
df = pd.read_csv("employees.csv")
result = df.groupby("Department")["Salary"].mean()
print(result)

# Common Aggregations
import pandas as pd
df = pd.read_csv("employees.csv")

# # Sum
df.groupby("Department")["Salary"].sum()
print(df.groupby("Department")["Salary"].sum())

# Average
df.groupby("Department")["Salary"].mean()
print(df.groupby("Department")["Salary"].mean())

# Count
df.groupby("Department")["Salary"].count()
print(df.groupby("Department")["Salary"].count())

# Minimum
df.groupby("Department")["Salary"].min()
print(df.groupby("Department")["Salary"].min())

# Maximum
df.groupby("Department")["Salary"].max()
print(df.groupby("Department")["Salary"].max())


import pandas as pd

# Read the employee dataset
df = pd.read_csv(r"D:\pandas_practice.py\employees_dataset.csv")

# Display the dataset
print("Employee Dataset:")
print(df)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Save the cleaned dataset
df.to_csv(
    r"D:\pandas_practice.py\cleaned_employees_dataset.csv",
    index=False
)

print("\nCleaned data exported successfully!")'''

import pandas as pd

# Read the employee dataset
df = pd.read_csv(r"D:\pandas_practice.py\employees_dataset.csv")

# Display the original dataset
print("Original Employee Dataset:")
print(df)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Display the cleaned dataset
print("\nCleaned Employee Dataset:")
print(df)

# Save the cleaned dataset
df.to_csv(
    r"D:\pandas_practice.py\cleaned_employees_dataset.csv",
    index=False
)

print("\nCleaned data exported successfully!")




