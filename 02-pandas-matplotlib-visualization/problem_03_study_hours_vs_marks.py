##########################    Problem No 03    ##########################

import pandas as pd
import matplotlib.pyplot as plt

def performance(marks):
    if marks >= 70:
        return "High"
    else:
        return "Low"

data = {
    "StudentID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "StudyHours": [2.0, 4.5, 6.0, 8.0, 2.5, 3.0, 7.5, 5.0, 9.0, 4.0, 1.5, 6.5, 10.0, 3.5, 8.5],
    "Marks": [45, 62, 75, 85, 90, 50, 78, 68, 92, -5, 35, 72, 120, 55, 88]
}

df = pd.DataFrame(data)

clean_df = df[(df["StudyHours"] >= 0) & (df["StudyHours"] <= 12) & (df["Marks"] >= 0) & (df["Marks"] <= 100)]
clean_df = clean_df.copy()

removed_rows = len(df) - len(clean_df)
print("Rows removed:", removed_rows)

print("\nCleaned data:")
print(clean_df)

performance_list = []
for m in clean_df["Marks"]:
    performance_list.append(performance(m))

clean_df["Performance"] = performance_list

high_df = clean_df[clean_df["Performance"] == "High"]
low_df = clean_df[clean_df["Performance"] == "Low"]

print("\nHigh performers:")
print(high_df)
print("\nLow performers:")
print(low_df)

high_avg_hours = high_df["StudyHours"].mean()
low_avg_hours = low_df["StudyHours"].mean()

print("\nAverage study hours - High:", high_avg_hours, "Low:", low_avg_hours)

plt.figure()
plt.scatter(high_df["StudyHours"], high_df["Marks"], color="green", label="High")
plt.scatter(low_df["StudyHours"], low_df["Marks"], color="red", label="Low")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.legend()
plt.show()

plt.figure()
plt.bar(["High", "Low"], [high_avg_hours, low_avg_hours], color=["green", "red"])
plt.xlabel("Performance Group")
plt.ylabel("Average Study Hours")
plt.title("Average Study Hours: High vs Low Performers")
plt.show()
