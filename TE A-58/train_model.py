import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
data = pd.read_csv("cancer_data.csv")

# Drop unnecessary columns
data = data.drop(columns=['index', 'Patient Id'])

# Encode target
data['Level'] = data['Level'].map({'Low': 0, 'Medium': 1, 'High': 2})

# Encode Gender
data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})

# Split features and target
X = data.drop(columns=['Level'])
y = data['Level']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train model
model = RandomForestClassifier()
model.fit(X_train_scaled, y_train)

# Save model and scaler
joblib.dump(model, 'train_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("✅ Model and scaler saved successfully.")
