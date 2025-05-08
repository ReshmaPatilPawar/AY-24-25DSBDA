import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("enhanced_song_dataset.csv")

# Encode mood labels
le = LabelEncoder()
df['mood_encoded'] = le.fit_transform(df['mood'])

# Save label encoder
joblib.dump(le, 'label_encoder.pkl')

# Features and labels
features = ['valence', 'danceability', 'energy', 'tempo', 'acousticness', 'liveness']
X = df[features]
y = df['mood_encoded']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, 'mood_predictor_model.pkl')
print("✅ Model saved successfully.")

# Save features list to ensure consistency during prediction
joblib.dump(features, 'model_features.pkl')
print("✅ Features list saved successfully.")
