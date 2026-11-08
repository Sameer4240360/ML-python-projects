###########################    Problem No 05    ##########################

import pandas as pd
import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self):
        self.categories = []
        self.amounts = []

    def add_expense(self, category, amount):
        self.categories.append(category)
        self.amounts.append(amount)

    def category_totals(self):
        df = pd.DataFrame({"Category": self.categories, "Amount": self.amounts})
        totals = {}
        for category in df["Category"].value_counts().index:
            totals[category] = df[df["Category"] == category]["Amount"].sum()
        return pd.Series(totals)

    def show_charts(self):
        totals = self.category_totals()
        sorted_totals = totals.sort_values(ascending=False)

        plt.figure()
        plt.pie(totals.values, labels=totals.index, autopct="%1.1f%%")
        plt.title("Category-wise Spending")
        plt.show()

        plt.figure()
        plt.bar(sorted_totals.index, sorted_totals.values)
        plt.xlabel("Category")
        plt.ylabel("Total Amount")
        plt.title("Sorted Category Totals")
        plt.show()

tracker = ExpenseTracker()

tracker.add_expense("Food", 1200)
tracker.add_expense("Food", 800)
tracker.add_expense("Food", 1500)
tracker.add_expense("Food", 900)

tracker.add_expense("Transport", 500)
tracker.add_expense("Transport", 700)
tracker.add_expense("Transport", 300)

tracker.add_expense("Books", 1800)
tracker.add_expense("Books", 600)

tracker.add_expense("Entertainment", 700)
tracker.add_expense("Entertainment", 500)

tracker.add_expense("Internet", 1000)
tracker.add_expense("Internet", 1000)

totals = tracker.category_totals()
print("Category totals:")
print(totals)

total_spending = totals.sum()
print("\nTotal spending:", total_spending)

shares = totals / total_spending * 100

sorted_totals = totals.sort_values(ascending=False)

print("\nCategories sorted (highest to lowest) with share:")
for category in sorted_totals.index:
    print(category, ":", sorted_totals[category], "-", "{:.2f}".format(shares[category]), "%")

for category in sorted_totals.index:
    if shares[category] > 30:
        print("\nWarning:", category, "takes more than 30% of total spending!")

tracker.show_charts()
