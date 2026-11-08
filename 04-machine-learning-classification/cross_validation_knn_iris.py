from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = iris.data
y = iris.target

model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=3))
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy")

for fold, score in enumerate(scores, start=1):
    print(f"Fold {fold} accuracy: {score:.2%}")

print(f"Average accuracy: {scores.mean():.2%}")
