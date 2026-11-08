# ##########################    Problem No 04    ##########################
import pandas as pd
import matplotlib.pyplot as plt

def day_type(temp):
    if temp < 18:
        return "Cold"
    elif temp <= 30:
        return "Pleasant"
    else:
        return "Hot"

data = {
    "Day": list(range(1, 31)),
    "Temp_C": [12, 14, 16, 19, 21, 23, 25,
               24, 26, 28, 30, 31, 33, 29,
               32, 35, 37, 38, 36, 34, 31,
               30, 28, 26, 24, 22, 20, 17,
               15, 13]
}

df = pd.DataFrame(data)

df["Temp_F"] = df["Temp_C"] * 9 / 5 + 32

daytype_list = []

for t in df["Temp_C"]:
    daytype_list.append(day_type(t))

df["DayType"] = daytype_list

print(df)

day_counts = df["DayType"].value_counts()
print("\nDay type counts:")
print(day_counts)

week1_avg = df.iloc[0:7]["Temp_C"].mean()
week2_avg = df.iloc[7:14]["Temp_C"].mean()
week3_avg = df.iloc[14:21]["Temp_C"].mean()
week4_avg = df.iloc[21:28]["Temp_C"].mean()

weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]
weekly_avgs = [week1_avg, week2_avg, week3_avg, week4_avg]

print("\nWeekly average temperatures (Celsius):")
for i in range(4):
    print(weeks[i], ":", weekly_avgs[i])

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(df["Day"], df["Temp_C"])
plt.xlabel("Day")
plt.ylabel("Temperature (C)")
plt.title("Daily Temperature")

plt.subplot(2, 2, 2)
plt.hist(df["Temp_C"], bins=6, edgecolor="black")
plt.xlabel("Temperature (C)")
plt.ylabel("Number of Days")
plt.title("Temperature Histogram")

plt.subplot(2, 2, 3)
plt.pie(day_counts.values, labels=day_counts.index, autopct="%1.1f%%")
plt.title("Day Type Distribution")

plt.subplot(2, 2, 4)
plt.bar(weeks, weekly_avgs)
plt.xlabel("Week")
plt.ylabel("Average Temperature (C)")
plt.title("Weekly Average Temperature")

plt.tight_layout()
plt.show()
