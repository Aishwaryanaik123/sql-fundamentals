import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# CREATE DATASET
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 14000, 18000, 21000, 25000],
    "Profit": [2000, 2500, 2200, 3200, 4000, 5000],
    "Customers": [120, 150, 140, 180, 210, 250]
}

df = pd.DataFrame(data)


# APPLY SEABORN THEME
sns.set_theme(style="whitegrid")



# 1. LINE CHAR
plt.figure(figsize=(8, 5))

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Sales")

# Data callouts
for i, value in enumerate(df["Sales"]):
    plt.annotate(
        str(value),
        (i, value),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center"
    )

plt.tight_layout()

# Save as PNG
plt.savefig("monthly_sales.png", dpi=300, bbox_inches="tight")

plt.show()



# 2. BAR CHART
plt.figure(figsize=(8, 5))

bars = plt.bar(
    df["Month"],
    df["Profit"]
)

plt.title("Monthly Profit", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Profit")

# Data callouts
for bar, value in zip(bars, df["Profit"]):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        str(value),
        ha="center",
        va="bottom"
    )

plt.tight_layout()

# Save as PNG
plt.savefig("monthly_profit.png", dpi=300, bbox_inches="tight")

plt.show()



# 3. SCATTER CHART
plt.figure(figsize=(8, 5))

plt.scatter(
    df["Customers"],
    df["Sales"],
    s=100
)

plt.title("Customers vs Sales", fontsize=16)
plt.xlabel("Number of Customers")
plt.ylabel("Sales")

# Data callouts
for i in range(len(df)):
    plt.annotate(
        df["Month"][i],
        (df["Customers"][i], df["Sales"][i]),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.tight_layout()

# Save as PNG
plt.savefig("customers_vs_sales.png", dpi=300, bbox_inches="tight")

plt.show()


# 4. HISTOGRAM
plt.figure(figsize=(8, 5))

plt.hist(
    df["Sales"],
    bins=5,
    edgecolor="black"
)

plt.title("Sales Distribution", fontsize=16)
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.tight_layout()

# Save as PNG
plt.savefig("sales_distribution.png", dpi=300, bbox_inches="tight")

plt.show()



# 5. BOX PLOT
plt.figure(figsize=(8, 5))

plt.boxplot(
    df["Sales"]
)

plt.title("Sales Box Plot", fontsize=16)
plt.xlabel("Sales")
plt.ylabel("Sales")

plt.tight_layout()

# Save as PNG
plt.savefig("sales_boxplot.png", dpi=300, bbox_inches="tight")

plt.show()


# COMPLETE
print("All charts created successfully!")
print("PNG files saved successfully!")