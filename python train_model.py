import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("C:/Users/RUCHITA/disease prediction dsbda/Diseases-Prediction-based-on-Symptoms/Dataset/dataset.csv")

# Clean column names and values
df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Encode the target column (Disease)
label_encoder = LabelEncoder()
df['Disease'] = label_encoder.fit_transform(df['Disease'])

# Save the label encoder for decoding predictions later
joblib.dump(label_encoder, 'label_encoder.pkl')

# Features and target
X = df.drop(columns=['Disease'])
y = df['Disease']

# Encode symptom strings to numerical values using another LabelEncoder (or load from Symptom-severity.csv)
# Instead, use Symptom-severity.csv directly if available (recommended)
for col in X.columns:
    if X[col].dtype == 'object':
        X[col] = X[col].astype(str).str.strip()

        # Optionally replace symptom strings with weights using Symptom-severity.csv
        severity = pd.read_csv("C:/Users/RUCHITA/disease prediction dsbda/Diseases-Prediction-based-on-Symptoms/Dataset/Symptom-severity.csv")
        severity['Symptom'] = severity['Symptom'].str.replace('_', ' ').str.strip()
        severity_dict = dict(zip(severity['Symptom'], severity['weight']))
        
        X[col] = X[col].map(severity_dict).fillna(0)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'model_RFC.pkl')

print("✅ Model trained and saved as model_RFC.pkl")
print("✅ Label encoder saved as label_encoder.pkl")
