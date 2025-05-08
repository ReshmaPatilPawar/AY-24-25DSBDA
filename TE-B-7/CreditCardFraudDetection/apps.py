import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("fraud_model.pkl")

model = load_model()

# Streamlit app layout
st.title("💳 Credit Card Fraud Detector")
st.markdown("### Detect fraudulent transactions using AI! Upload a dataset or enter details manually.")

# Sidebar Instructions
st.sidebar.title("📌 How to Use")
st.sidebar.write("1️⃣ Upload a CSV file containing credit card transactions.")
st.sidebar.write("2️⃣ The model will analyze the data and classify transactions as fraudulent or safe.")
st.sidebar.write("3️⃣ View results instantly in the table below!")

# **📤 File uploader for dataset**
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    # Read the dataset dynamically
    df = pd.read_csv(uploaded_file)

    # **Extract relevant features (Amount, Time)**
    features = df[['Amount', 'Time']].values  # Removed PCA components

    # **Predict fraud for all transactions**
    predictions = model.predict(features)

    # **Add predictions to the dataset**
    df["Fraud Prediction"] = ["🚨 Fraud" if pred >= 0.5 else "✅ Safe" for pred in predictions]

    # **Display prediction results**
    st.subheader("🔎 Prediction Results")
    st.write(df)

    # **📊 Fraud Statistics**
    fraud_count = sum(predictions)
    safe_count = len(predictions) - fraud_count

    # **📈 Pie Chart for Fraud Analysis**
    fig, ax = plt.subplots()
    ax.pie([safe_count, fraud_count], labels=["Safe Transactions", "Fraudulent Transactions"], autopct="%1.1f%%", colors=["green", "red"])
    st.subheader("📊 Fraud Detection Summary")
    st.pyplot(fig)

    # **📂 Export Fraud Predictions to CSV**
    st.subheader("📥 Save Fraud Predictions")
    if st.button("Export to CSV"):
        df.to_csv("fraud_detection_results.csv", index=False)
        st.success("✅ Fraud predictions saved as 'fraud_detection_results.csv'!")

# **🔍 Quick Single Transaction Checker**
st.markdown("### 🔍 Quick Transaction Check")
single_amount = st.number_input("Transaction Amount", value=100.0, step=10.0)
single_time = st.number_input("Transaction Time", value=50000, step=1000)

if st.button("🔍 Check This Transaction"):
    input_data = np.array([[single_amount, single_time]])  # Removed PCA components
    single_prediction = model.predict_proba(input_data)[0][1]  # Get fraud probability

    st.subheader("Prediction Result")
    if single_prediction >= 0.5:
        st.error(f"🚨 High risk of fraud! ({single_prediction*100:.2f}% probability)")
    else:
        st.success(f"✅ Low risk of fraud ({single_prediction*100:.2f}% probability)")
