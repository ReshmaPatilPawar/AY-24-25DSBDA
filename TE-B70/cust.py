import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import mean_squared_error, r2_score

# Load and clean data
@st.cache_data
def load_data():
    df = pd.read_csv("unclean_customer_data.csv")

    # Drop rows with missing values
    df = df.dropna()

    # Encode categorical columns
    le = LabelEncoder()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = le.fit_transform(df[col].astype(str))

    return df

# ---------------- APP START ----------------
st.title("📊 Customer Data Prediction App with Visualizations")

df = load_data()
st.write("✅ Cleaned Dataset Preview:")
st.dataframe(df.head())

# Target selection
target_col = st.selectbox("🎯 Select the target variable", df.columns)
X = df.drop(columns=[target_col])
y = df[target_col]

# Detect task type
task_type = "classification" if y.nunique() < 20 and y.dtype in ['int64', 'int32'] else "regression"
st.markdown(f"**Detected Task Type:** `{task_type.capitalize()}`")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model training
model = RandomForestClassifier() if task_type == "classification" else RandomForestRegressor()
model.fit(X_train, y_train)
st.success("✅ Model Trained Successfully!")

# ---------------- DATA VISUALIZATION ----------------
if st.checkbox("📈 Show Data Visualizations"):
    st.subheader("🔗 Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)

    st.subheader("📊 Target Variable Distribution")
    if task_type == "classification":
        st.bar_chart(y.value_counts())
    else:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(y, kde=True, ax=ax)
        st.pyplot(fig)

    st.subheader("📌 Feature Importance")
    importances = model.feature_importances_
    feat_imp_df = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
    feat_imp_df = feat_imp_df.sort_values(by="Importance", ascending=False)
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.barplot(x='Importance', y='Feature', data=feat_imp_df, ax=ax)
    st.pyplot(fig)

# ---------------- MODEL EVALUATION ----------------
if st.checkbox("📋 Show Model Evaluation on Test Data"):
    y_pred = model.predict(X_test)

    if task_type == "classification":
        st.subheader("📊 Confusion Matrix")
        fig, ax = plt.subplots()
        ConfusionMatrixDisplay.from_predictions(y_test, y_pred, cmap="Blues", ax=ax)
        st.pyplot(fig)

        st.subheader("📄 Classification Report")
        st.text(classification_report(y_test, y_pred))
    else:
        st.subheader("📈 Actual vs Predicted")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.scatterplot(x=y_test, y=y_pred, ax=ax)
        ax.set_xlabel("Actual")
        ax.set_ylabel("Predicted")
        st.pyplot(fig)

        st.write("**Mean Squared Error:**", mean_squared_error(y_test, y_pred))
        st.write("**R² Score:**", r2_score(y_test, y_pred))

# ---------------- PREDICTION SECTION ----------------
data_source = st.radio("🗂 Choose data to predict on:", ["Training Data", "Testing Data"])
data_to_predict = X_train if data_source == "Training Data" else X_test

if st.button("🔮 Predict"):
    preds = model.predict(data_to_predict)
    result_df = data_to_predict.copy()
    result_df["Prediction"] = preds
    st.write("📄 Data with Predictions:")
    st.dataframe(result_df)
