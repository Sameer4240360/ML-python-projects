#################              Question 2: Naive Bayes Classification    #################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("naive_bayes_scholarship_dataset.csv")

X = df[["CGPA", "Attendance", "FamilyIncome_Thousands"]]

y = df["Category"]

valid_data = X.notna().all(axis=1)

X = X[valid_data]

y = y[valid_data]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = GaussianNB()

model.fit(X_train, y_train)

new_student = [[3.3, 86, 42]]

prediction = model.predict(new_student)

probabilities = model.predict_proba(new_student)

print("Predicted Category:", prediction[0])

print("Probabilities:", probabilities[0])

print("Categories:", model.classes_)
