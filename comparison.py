import pandas as pd

# Load dataset
df = pd.read_csv("data/indian_covid19.csv")

# Remove aggregate Total row
df = df[df["State"] != "Total"].copy()

print("PandasAI vs Manual Pandas Comparison")
print("=" * 60)

# Question 1
question1 = "Which state has the highest confirmed cases?"
manual1 = df.loc[df["Confirmed"].idxmax(), "State"]

# Question 2
question2 = "Which state has the highest number of deaths?"
manual2 = df.loc[df["Deaths"].idxmax(), "State"]

# Question 3
question3 = "Which state has the highest number of active cases?"
manual3 = df.loc[df["Active"].idxmax(), "State"]

print("\nQuestion 1:", question1)
print("Manual Pandas Answer:", manual1)
print("PandasAI Answer: Pending API credits")

print("\nQuestion 2:", question2)
print("Manual Pandas Answer:", manual2)
print("PandasAI Answer: Pending API credits")

print("\nQuestion 3:", question3)
print("Manual Pandas Answer:", manual3)
print("PandasAI Answer: Pending API credits")