
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression

# Load and preprocess the data
df = pd.read_csv("cricket_data_2025.csv")
df = df.dropna()

# Encode categorical columns
le_dict = {}
for column in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    le_dict[column] = le

# Split data
X = df.drop(['Batting_Average'], axis=1)
y = df['Batting_Strike_Rate']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the model
model = LinearRegression()
model.fit(X_scaled, y)

# Build Streamlit app
st.title("🏏 Cricket Strike Rate Predictor")
st.write("Enter player stats below to predict their batting strike rate.")

# Create dynamic inputs
user_data = {}
for col in X.columns:
    if col in le_dict:
        options = le_dict[col].classes_.tolist()
        user_data[col] = st.selectbox(col, options)
    else:
        user_data[col] = st.number_input(col, step=1.0)

# Prediction
if st.button("Predict"):
    # Transform inputs
    input_df = pd.DataFrame([user_data])
    for col, le in le_dict.items():
        input_df["Batting_Average"] = le.transform(input_df["Batting_Average"])

    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]

    st.success(f"🏆 Predicted Batting Strike Rate: **{prediction:.2f}**")
