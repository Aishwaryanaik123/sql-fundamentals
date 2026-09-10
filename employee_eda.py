import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. LOAD DATASET
df = pd.read_csv("Employee.csv")

print("========== DATASET PROFILE ==========")

print("Shape:", df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nNull Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())



# 2. SUMMARY STATISTICS
print("\n========== SUMMARY STATISTICS ==========")

summary = df.describe()

print(summary)



# 3. DISTRIBUTION OF NUMERIC COLUMNS
numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    plt.figure(figsize=(8, 5))

    sns.histplot(df[column], kde=True)

    plt.title("Distribution of " + column)
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()



# 4. CORRELATION MATRIX

correlation = df[numeric_columns].corr()
print("\n========== CORRELATION MATRIX ==========")
print(correlation)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()



# 5. BUSINESS INSIGHT 1
# Leave Rate by City
city_leave = df.groupby("City")["LeaveOrNot"].mean() * 100

print("\nLeave Rate by City:")
print(city_leave)

plt.figure(figsize=(8, 5))

city_leave.plot(kind="bar")

plt.title("Employee Leave Rate by City")
plt.xlabel("City")
plt.ylabel("Leave Rate (%)")

plt.tight_layout()
plt.show()



# 6. BUSINESS INSIGHT 2
# Leave Rate by Payment Tier
tier_leave = df.groupby("PaymentTier")["LeaveOrNot"].mean() * 100

print("\nLeave Rate by Payment Tier:")
print(tier_leave)

plt.figure(figsize=(8, 5))

tier_leave.plot(kind="bar")

plt.title("Employee Leave Rate by Payment Tier")
plt.xlabel("Payment Tier")
plt.ylabel("Leave Rate (%)")

plt.tight_layout()
plt.show()



# 7. BUSINESS INSIGHT 3
# Leave Rate by Education
education_leave = df.groupby("Education")["LeaveOrNot"].mean() * 100

print("\nLeave Rate by Education:")
print(education_leave)

plt.figure(figsize=(8, 5))

education_leave.plot(kind="bar")

plt.title("Employee Leave Rate by Education")
plt.xlabel("Education")
plt.ylabel("Leave Rate (%)")

plt.tight_layout()
plt.show()



# 8. BUSINESS INSIGHT 4
# Leave Rate by Gender
gender_leave = df.groupby("Gender")["LeaveOrNot"].mean() * 100

print("\nLeave Rate by Gender:")
print(gender_leave)

plt.figure(figsize=(8, 5))

gender_leave.plot(kind="bar")

plt.title("Employee Leave Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Leave Rate (%)")

plt.tight_layout()
plt.show()



# 9. BUSINESS INSIGHT 5
# Leave Rate by Bench Status
bench_leave = df.groupby("EverBenched")["LeaveOrNot"].mean() * 100

print("\nLeave Rate by Bench Status:")
print(bench_leave)

plt.figure(figsize=(8, 5))

bench_leave.plot(kind="bar")

plt.title("Employee Leave Rate by Bench Status")
plt.xlabel("Ever Benched")
plt.ylabel("Leave Rate (%)")

plt.tight_layout()
plt.show()


# 10. OVERALL LEAVE RATE
overall_leave_rate = df["LeaveOrNot"].mean() * 100

print("\n========== OVERALL LEAVE RATE ==========")
print("Overall Employee Leave Rate:",
      round(overall_leave_rate, 2), "%")


print("\nEDA COMPLETED SUCCESSFULLY!")