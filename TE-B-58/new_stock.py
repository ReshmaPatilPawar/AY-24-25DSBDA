import streamlit as st
import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# ------------------- Streamlit Config -------------------
st.set_page_config(page_title="Adani Ports Predictor", page_icon="📊", layout="wide")

# ------------------- Custom CSS Styling -------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #e0f7fa, #ffffff);
    }
    .main > div {
        padding-top: 2rem;
    }
    h1 {
        color: #0077b6 !important;
        text-align: center;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 18px;
        padding: 8px 16px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------- Load Dataset -------------------
@st.cache_data
def load_data():
    df = pd.read_csv("ADANIPORTS.csv")
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# ------------------- Sidebar -------------------
st.sidebar.header("🛠️ Configuration Panel")
numeric_cols = df.select_dtypes(include='number').columns.tolist()
date_col = "Date" if "Date" in df.columns else None

target_col = st.sidebar.selectbox("🎯 Target Variable", numeric_cols)
feature_col = st.sidebar.selectbox("📈 Feature Variable", [col for col in numeric_cols if col != target_col])
test_size_percent = st.sidebar.slider("🔀 Test Size (%)", 10, 50, 20)
show_data = st.sidebar.checkbox("📄 Show Raw Data", True)

# Date filtering
if date_col:
    df[date_col] = pd.to_datetime(df[date_col])
    min_date, max_date = df[date_col].min(), df[date_col].max()

    st.sidebar.subheader("📅 Select Date Range")
    selected_dates = st.sidebar.date_input("Date range", [min_date, max_date],
                                           min_value=min_date, max_value=max_date)

    if isinstance(selected_dates, list) and len(selected_dates) == 2:
        start_date, end_date = selected_dates
        df = df[(df[date_col] >= pd.to_datetime(start_date)) & (df[date_col] <= pd.to_datetime(end_date))]
        df.set_index(date_col, inplace=True)
    else:
        st.warning("⚠️ Please select both a start and end date!")

# ------------------- Main UI -------------------
st.markdown("<h1>📊 Adani Ports Stock Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("---")

# Show raw data
if show_data:
    st.subheader("📂 Raw Data Preview")
    st.dataframe(df.head(15), height=250)

# Spinner while training
with st.spinner("🚀 Training the model..."):
    time.sleep(0.5)
    X = df[[feature_col]]
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_percent / 100, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    train_preds = model.predict(X_train)
    test_preds = model.predict(X_test)

# ------------------- Charts -------------------
st.markdown("### 📈 Predictions Overview")
tab1, tab2 = st.tabs(["Training Predictions", "Testing Predictions"])

with tab1:
    st.write("Actual vs Predicted (Training)")
    st.line_chart(pd.DataFrame({"Actual": y_train.values, "Predicted": train_preds}, index=y_train.index))

with tab2:
    st.write("Actual vs Predicted (Testing)")
    st.line_chart(pd.DataFrame({"Actual": y_test.values, "Predicted": test_preds}, index=y_test.index))

# ------------------- Metrics -------------------
st.markdown("### 📊 Performance Metrics")
col1, col2 = st.columns(2)
with col1:
    st.metric("📘 Train MSE", f"{mean_squared_error(y_train, train_preds):.2f}")
with col2:
    st.metric("📕 Test MSE", f"{mean_squared_error(y_test, test_preds):.2f}")

# ------------------- Footer -------------------
# st.markdown("""
#     <hr>
#     <p style='text-align:center; color: gray;'>
#         Built with ❤️ by Pranav | Powered by Linear Regression
#     </p>
# """, unsafe_allow_html=True)
