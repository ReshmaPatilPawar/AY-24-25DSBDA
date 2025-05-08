# heart_app.py

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("heart.csv")

data = load_data()

# Show basic info
st.title("Heart Disease Predictor")
st.write("Dataset preview:")
st.dataframe(data.head())

# Prepare model
X = data.drop(columns='target', axis=1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=2)

model = LogisticRegression()
model.fit(X_train, y_train)

st.subheader("Model Accuracy")
train_acc = accuracy_score(model.predict(X_train), y_train)
test_acc = accuracy_score(model.predict(X_test), y_test)
st.write(f"Training Accuracy: {train_acc:.2f}")
st.write(f"Testing Accuracy: {test_acc:.2f}")

# User Input
st.subheader("Enter Patient Data")

def user_input():
    age = st.slider("Age", 20, 80, 50)
    sex = st.selectbox("Sex (1=Male, 0=Female)", [1, 0])
    cp = st.slider("Chest Pain Type (0-3)", 0, 3, 0)
    trestbps = st.slider("Resting Blood Pressure", 90, 200, 130)
    chol = st.slider("Cholesterol", 100, 600, 250)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)", [1, 0])
    restecg = st.slider("Resting ECG (0-2)", 0, 2, 1)
    thalach = st.slider("Max Heart Rate Achieved", 70, 210, 150)
    exang = st.selectbox("Exercise Induced Angina (1=Yes, 0=No)", [1, 0])
    oldpeak = st.slider("ST depression", 0.0, 6.0, 1.0)
    slope = st.slider("Slope of peak exercise ST segment (0-2)", 0, 2, 1)
    ca = st.slider("Number of major vessels (0-3)", 0, 3, 0)
    thal = st.slider("Thalassemia (0=Normal; 1=Fixed defect; 2=Reversable defect)", 0, 2, 1)
    
    return np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                      thalach, exang, oldpeak, slope, ca, thal]])

input_data = user_input()

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)
    result = "has Heart Disease" if prediction[0] == 1 else "does NOT have Heart Disease"
    st.success(f"The model predicts that the patient {result}.")
