import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib
import os

# Load dataset
df = pd.read_csv("dataset/imdb_movies.csv")

# Select features and target
X = df[['genre', 'director', 'budget', 'year', 'runtime']]
y = df['rating']

# Preprocessing
categorical = ['genre', 'director']
numeric = ['budget', 'year', 'runtime']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical),
    ('num', 'passthrough', numeric)
])

model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train the model
model.fit(X, y)

# Save the model
os.makedirs("backend/model", exist_ok=True)
joblib.dump(model, 'backend/model/imdb_model.pkl')

print("✅ Model trained and saved to backend/model/imdb_model.pkl")
