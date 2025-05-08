import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

# Load dataset
file_path = r"C:\Users\saura\OneDrive\Desktop\DSProject\wp\pune.csv"
df = pd.read_csv(file_path)

# Convert date column
df['date_time'] = pd.to_datetime(df['date_time'])
df['year'] = df['date_time'].dt.year
df['month'] = df['date_time'].dt.month
df['day'] = df['date_time'].dt.day
df.drop(columns=['date_time', 'moonrise', 'moonset', 'sunrise', 'sunset', 'location'], inplace=True)

# Define features and target
X = df.drop(columns=["maxtempC", "mintempC", "windspeedKmph", "humidity", "precipMM"])
y = df[["maxtempC", "mintempC", "windspeedKmph", "humidity", "precipMM"]]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
xgb_model = XGBRegressor(objective="reg:squarederror", n_estimators=100, random_state=42)
xgb_model.fit(X_train, y_train)

# Save model
model_path = r"C:\Users\saura\OneDrive\Desktop\DSProject\wp\xgboost\model.pkl"
joblib.dump(xgb_model, model_path)
print("XGBoost model trained and saved successfully!")
