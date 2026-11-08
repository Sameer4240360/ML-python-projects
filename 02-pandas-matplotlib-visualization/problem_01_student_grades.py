###########################    Problem No 01    ##########################
import pandas as pd
import matplotlib.pyplot as plt

def get_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40 :
        return "C"
    else:
        return "F"

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Hina", "Usman", "Ayesha", "Bilal", "Zainab", "Hamza", "Fatima"],
    "Math": [85, 92, 70, 55, 30, 78, 45, 66, 38, 88],
    "Science": [90, 88, 65, 48, 35, 82, 50, 72, 25, 76],
    "English": [78, 95, 72, 60, 28, 80, 42, 61, 40, 90]
}

df = pd.DataFrame(data)

df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Percentage"] = df["Total"] / 3

grades = []
for p in df["Percentage"]:
    grades.append(get_grade(p))
df["Grade"] = grades

print(df)

grade_counts = df["Grade"].value_counts()
print("\nGrade counts:")
print(grade_counts)

plt.figure()
plt.pie(grade_counts.values, labels=grade_counts.index, autopct="%1.1f%%")
plt.title("Grade Distribution")
plt.show()

plt.figure()
plt.hist(df["Percentage"], bins=5, edgecolor="black")
plt.xlabel("Percentage")
plt.ylabel("Number of Students")
plt.title("Histogram of Percentage")
plt.show()
