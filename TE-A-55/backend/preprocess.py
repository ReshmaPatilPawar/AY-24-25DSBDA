import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
import joblib

# Load dataset
df = pd.read_csv("../electric dataset.csv")  
# Convert 'Datetime' column and extract time features
if 'Datetime' in df.columns:
    df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce')
    df['Hour'] = df['Datetime'].dt.hour
    df['Day'] = df['Datetime'].dt.day
    df['Month'] = df['Datetime'].dt.month
else:
    raise ValueError("❌ Missing 'Datetime' column in dataset.")

# Define feature and target columns
features = ['Temperature', 'Humidity', 'WindSpeed', 'GeneralDiffuseFlows', 'DiffuseFlows', 'Hour', 'Day', 'Month']
targets = ['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3']

# Drop rows with missing values
df.dropna(subset=features + targets, inplace=True)

# Split features and targets
X = df[features]
y = df[targets]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=42))
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model.pkl')
print("✅ Model trained and saved as model.pkl")
