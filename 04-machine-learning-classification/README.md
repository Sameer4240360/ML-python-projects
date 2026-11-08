# 04 - Machine Learning Classification

| File | What it does |
|---|---|
| `knn_loan_risk.py` | KNN predicts loan risk for a new applicant (K=3), compares it with scaled features, and tests K = 1, 3, 5, 7 on a train/test split |
| `naive_bayes_scholarship.py` | Gaussian Naive Bayes predicts a scholarship category and prints class probabilities |
| `cross_validation_knn_iris.py` | 5-fold stratified cross-validation of a scaled KNN pipeline on the Iris dataset |
| `phones_sales_category_knn.py` | KNN with a preprocessing pipeline (one-hot encoding for brand, scaling for numbers) predicting a phone's sales category |

**Run:** `python cross_validation_knn_iris.py` works as it is (it uses the built-in Iris dataset).

The other scripts read CSV files that are **not included in this repository**. Put these files in this folder before running:

| Script | Expected file | Columns used |
|---|---|---|
| `knn_loan_risk.py` | `knn_loan_risk_dataset - knn_loan_risk_dataset.csv` | `AnnualIncome_Thousands`, `ExistingDebt_Thousands`, `Risk` |
| `naive_bayes_scholarship.py` | `naive_bayes_scholarship_dataset.csv` | `CGPA`, `Attendance`, `FamilyIncome_Thousands`, `Category` |
| `phones_sales_category_knn.py` | `PhonesData.csv` | `brand`, `ram`, `storage`, `battery`, `price`, `salesCategory` |

**Concepts:** train/test split, feature scaling, choosing K, accuracy, probabilities, cross-validation, pipelines
