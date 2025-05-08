import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv('./data/Student_performance_data.csv')

# Drop missing values
df.dropna(inplace=True)

# Target column for regression
target_col = 'GPA'

# Drop target and non-feature columns
X = df.drop(columns=['StudentID', target_col])
y = df[target_col]

# One-hot encode categorical variables
X = pd.get_dummies(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(f"R² Score: {r2_score(y_test, y_pred):.4f}")

# Save model and columns
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/model.pkl')
joblib.dump(X.columns.tolist(), 'models/columns.pkl')
