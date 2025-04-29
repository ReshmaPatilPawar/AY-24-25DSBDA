import pandas as pd
import joblib
from sklearn.metrics import r2_score

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

# Load models
models = {
    "Linear Regression": joblib.load(r"C:\Users\saura\OneDrive\Desktop\DSProject\wp\linear_regression\model.pkl"),
    "Random Forest": joblib.load(r"C:\Users\saura\OneDrive\Desktop\DSProject\wp\random_forest\model.pkl"),
    "XGBoost": joblib.load(r"C:\Users\saura\OneDrive\Desktop\DSProject\wp\xgboost\model.pkl")
}

# Evaluate each model
for name, model in models.items():
    y_pred = model.predict(X)
    accuracy = r2_score(y, y_pred) * 100  # Convert to percentage
    print(f"{name} Accuracy: {accuracy:.2f}%")
