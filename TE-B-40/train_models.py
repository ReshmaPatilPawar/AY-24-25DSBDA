import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset (make sure shopping_trends.csv is in your project folder)
df = pd.read_csv("shopping_trends.csv")

# Remove the ID column (not needed for predictions)
df.drop(columns=["Customer ID"], inplace=True)

# Prepare label encoders for all categorical columns
label_encoders = {}
categorical_columns = df.select_dtypes(include=["object"]).columns

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Separate features from targets:
#  - For classification: we predict 'Discount Applied'
#  - For regression: we predict 'Purchase Amount (USD)'
X = df.drop(columns=["Discount Applied", "Purchase Amount (USD)"])
y_class = df["Discount Applied"]
y_reg = df["Purchase Amount (USD)"]

# Split data (using the same X for both models)
X_train, X_test, y_train_class, y_test_class = train_test_split(
    X, y_class, test_size=0.2, random_state=42
)
# For regression; using the same split for simplicity
_, _, y_train_reg, y_test_reg = train_test_split(
    X, y_reg, test_size=0.2, random_state=42
)

# Initialize and train models
classifier = RandomForestClassifier(random_state=42)
regressor = RandomForestRegressor(random_state=42)

classifier.fit(X_train, y_train_class)
regressor.fit(X_train, y_train_reg)

# Save models and encoders using joblib
joblib.dump(classifier, "classifier.pkl")
joblib.dump(regressor, "regressor.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")

print("Models and encoders have been saved successfully!")
