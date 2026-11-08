##########################    Problem No 02    ##########################

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Revenue": [50000, 45000, 52000, 58000, 61000, 55000, 48000, 53000, 60000, 66000, 72000, 80000],
    "Cost": [42000, 47000, 45000, 46000, 50000, 52000, 51000, 49000, 47000, 51000, 58000, 62000]
}

df = pd.DataFrame(data)

df["Profit"] = df["Revenue"] - df["Cost"]

print(df)

best_profit = df["Profit"].max()
worst_profit = df["Profit"].min()

best_month = df[df["Profit"] == best_profit]["Month"].iloc[0]
worst_month = df[df["Profit"] == worst_profit]["Month"].iloc[0]

print("\nBest month:", best_month, "with profit", best_profit)
print("Worst month:", worst_month, "with profit", worst_profit)

q1_revenue = df.iloc[0:3]["Revenue"].sum()
q1_cost = df.iloc[0:3]["Cost"].sum()
q2_revenue = df.iloc[3:6]["Revenue"].sum()
q2_cost = df.iloc[3:6]["Cost"].sum()
q3_revenue = df.iloc[6:9]["Revenue"].sum()
q3_cost = df.iloc[6:9]["Cost"].sum()
q4_revenue = df.iloc[9:12]["Revenue"].sum()
q4_cost = df.iloc[9:12]["Cost"].sum()

quarters = ["Q1", "Q2", "Q3", "Q4"]
quarter_revenue = [q1_revenue, q2_revenue, q3_revenue, q4_revenue]
quarter_cost = [q1_cost, q2_cost, q3_cost, q4_cost]

print("\nQuarterly totals:")
for i in range(4):
    print(quarters[i], "- Revenue:", quarter_revenue[i], "Cost:", quarter_cost[i])

plt.figure()
plt.plot(df["Month"], df["Profit"], marker="o")
plt.scatter(best_month, best_profit, color="red", s=100)
plt.text(best_month, best_profit, "Best Month ", color="red", ha="right")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.title("Monthly Profit")
plt.show()

plt.figure()
revenue_positions = [i - 0.2 for i in range(4)]
cost_positions = [i + 0.2 for i in range(4)]
plt.bar(revenue_positions, quarter_revenue, width=0.4, label="Revenue")
plt.bar(cost_positions, quarter_cost, width=0.4, label="Cost")
plt.xticks(range(4), quarters)
plt.xlabel("Quarter")
plt.ylabel("Amount")
plt.title("Quarterly Revenue vs Cost")
plt.legend()
plt.show()
