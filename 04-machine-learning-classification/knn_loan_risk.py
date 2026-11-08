###############     Question 1: K-Nearest Neighbors (KNN)    #####################
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


df = pd.read_csv("knn_loan_risk_dataset - knn_loan_risk_dataset.csv")

X = df[["AnnualIncome_Thousands", "ExistingDebt_Thousands"]]
y = df["Risk"]

print(df)

valid_data = X.notna().all(axis=1)

X = X[valid_data]
y = y[valid_data]

new_applicant = [[43, 14]]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

prediction = model.predict(new_applicant)

print("K=3 Prediction:", prediction[0])

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
new_applicant_scaled = scaler.transform(new_applicant)

scaled_model = KNeighborsClassifier(n_neighbors=3)
scaled_model.fit(X_scaled, y)

scaled_prediction = scaled_model.predict(new_applicant_scaled)

print("Scaled K=3 Prediction:", scaled_prediction[0])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

k_values = [1, 3, 5, 7]

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print("K =", k, "Accuracy =", accuracy)
