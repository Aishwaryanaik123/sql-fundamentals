import pandas as pd

# TASK 1: Merge two DataFrames using all join types
# First DataFrame
df1 = pd.DataFrame({
    "Employee_ID": [1, 2, 3, 4],
    "Name": ["Asha", "Rahul", "Priya", "Kiran"],
    "Region": ["North", "South", "East", "West"]
})

# Second DataFrame
df2 = pd.DataFrame({
    "Employee_ID": [2, 3, 4, 5],
    "Sales": [50000, 60000, 45000, 70000],
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop"]
})

print("========== DATAFRAME 1 ==========")
print(df1)

print("\n========== DATAFRAME 2 ==========")
print(df2)


# INNER JOIN
inner_join = pd.merge(df1, df2, on="Employee_ID", how="inner")

print("\n========== INNER JOIN ==========")
print(inner_join)


# LEFT JOIN
left_join = pd.merge(df1, df2, on="Employee_ID", how="left")

print("\n========== LEFT JOIN ==========")
print(left_join)


# RIGHT JOIN
right_join = pd.merge(df1, df2, on="Employee_ID", how="right")

print("\n========== RIGHT JOIN ==========")
print(right_join)


# OUTER JOIN
outer_join = pd.merge(df1, df2, on="Employee_ID", how="outer")

print("\n========== OUTER JOIN ==========")
print(outer_join)



# TASK 2: Create a Pivot Table
sales_data = pd.DataFrame({
    "Region": ["North", "North", "South", "South",
               "East", "East", "West", "West"],
    "Product": ["Laptop", "Mobile", "Laptop", "Mobile",
                "Laptop", "Mobile", "Laptop", "Mobile"],
    "Sales": [50000, 30000, 45000, 35000,
              60000, 40000, 55000, 25000]
})

print("\n========== SALES DATA ==========")
print(sales_data)

pivot_table = pd.pivot_table(
    sales_data,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum",
    fill_value=0
)

print("\n========== PIVOT TABLE ==========")
print(pivot_table)



# TASK 3: Use pd.melt() to reshape wide data to long format
wide_data = pd.DataFrame({
    "Employee": ["Asha", "Rahul", "Priya"],
    "January": [50000, 45000, 60000],
    "February": [55000, 48000, 65000],
    "March": [58000, 50000, 70000]
})

print("\n========== WIDE DATA ==========")
print(wide_data)

long_data = pd.melt(
    wide_data,
    id_vars=["Employee"],
    var_name="Month",
    value_name="Sales"
)

print("\n========== LONG DATA USING MELT ==========")
print(long_data)



# TASK 4: Method Chaining
method_chain_result = (
    sales_data
    .query("Sales > 40000")
    .sort_values("Sales", ascending=False)
    [["Region", "Product", "Sales"]]
    .reset_index(drop=True)
)

print("\n========== METHOD CHAINING RESULT ==========")
print(method_chain_result)