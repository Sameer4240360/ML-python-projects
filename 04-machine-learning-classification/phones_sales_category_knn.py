from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DATA_FILE = Path(__file__).with_name("PhonesData.csv")
FEATURES = ["brand", "ram", "storage", "battery", "price"]
NUMERIC_FEATURES = ["ram", "storage", "battery", "price"]
TARGET = "salesCategory"
K_NEIGHBORS = 1


data = pd.read_csv(DATA_FILE)

missing_columns = set(FEATURES + [TARGET]) - set(data.columns)
if missing_columns:
    raise ValueError(f"CSV is missing required columns: {sorted(missing_columns)}")
if data.empty:
    raise ValueError("PhonesData.csv must contain at least one data row.")

X = data[FEATURES]
y = data[TARGET]

preprocessor = ColumnTransformer(
    transformers=[
        ("brand", OneHotEncoder(handle_unknown="ignore"), ["brand"]),
        ("numbers", StandardScaler(), NUMERIC_FEATURES),
    ]
)

model = make_pipeline(
    preprocessor,
    KNeighborsClassifier(n_neighbors=min(K_NEIGHBORS, len(data))),
)
model.fit(X, y)

new_phone = pd.DataFrame(
    [
        {
            "brand": input("Brand: ").strip(),
            "ram": float(input("RAM (GB): ")),
            "storage": float(input("Storage (GB): ")),
            "battery": float(input("Battery (mAh): ")),
            "price": float(input("Price: ")),
        }
    ],
    columns=FEATURES,
)

prediction = model.predict(new_phone)[0]
print(f"Predicted sales category: {prediction}")
