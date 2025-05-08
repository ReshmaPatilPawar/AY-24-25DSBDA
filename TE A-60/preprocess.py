import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from difflib import get_close_matches

# Step 1: Load dataset
df = pd.read_csv('city_day 1.csv')
print("📋 Columns in dataset:", df.columns.tolist())

# Step 2: Identify actual PM2.5 column
possible_targets = get_close_matches('pm2_5', df.columns, n=3, cutoff=0.3)
if not possible_targets:
    raise ValueError("Couldn't find a column similar to 'pm2_5'. Please check column names.")
target_col = possible_targets[0]
print(f"🎯 Using '{target_col}' as target variable.")

# Step 3: Drop unusable or irrelevant columns
df.drop(columns=['id', 'location'], inplace=True, errors='ignore')

# Step 4: Drop missing values
df.dropna(inplace=True)

# Step 5: Detect and process date column
possible_date_cols = [col for col in df.columns if 'date' in col.lower()]
if possible_date_cols:
    date_col = possible_date_cols[0]
    df[date_col] = pd.to_datetime(df[date_col])
    df['year'] = df[date_col].dt.year
    df['month'] = df[date_col].dt.month
    df.drop(columns=[date_col], inplace=True)

# Step 6: Encode categorical columns
cat_cols = df.select_dtypes(include='object').columns.tolist()
print(f"🔤 Encoding categorical columns: {cat_cols}")
df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

# Step 7: Prepare features and target
X = df.drop(columns=[target_col])
y = df[target_col]

# Step 8: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 9: Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 10: Predict and evaluate
y_pred = model.predict(X_test)
print("\n✅ Model Evaluation:")
print(f"R² Score: {r2_score(y_test, y_pred):.3f}")
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse:.3f}")

# Step 11: Save model and column names
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model_columns.pkl', 'wb') as f:
    pickle.dump(X.columns.tolist(), f)

print("✅ Model and feature columns saved successfully.")
