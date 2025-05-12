import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

st.set_page_config(page_title="🩺 Diabetes Prediction App", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("diabetes_prediction_dataset.csv")
    return df

df = load_data()

st.title("🩺 Diabetes Prediction Using Machine Learning")

# Sidebar - Show data
st.sidebar.header("🗂 Options")
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("📄 Full Dataset")
    st.dataframe(df)

# Encode categorical features
df_encoded = df.copy()
label_encoders = {}
for col in df_encoded.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col])
    label_encoders[col] = le

# Features and target
X = df_encoded.drop("diabetes", axis=1)
y = df_encoded["diabetes"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Sidebar - Prediction choice
st.sidebar.subheader("📊 Prediction on Data")
data_choice = st.sidebar.radio("Choose data:", ["Training Data", "Testing Data"])

if data_choice == "Training Data":
    y_pred = model.predict(X_train)
    st.subheader("🧪 Prediction on Training Data")
    st.write("Accuracy:", accuracy_score(y_train, y_pred))
    st.text(classification_report(y_train, y_pred))
elif data_choice == "Testing Data":
    y_pred = model.predict(X_test)
    st.subheader("🧪 Prediction on Testing Data")
    st.write("Accuracy:", accuracy_score(y_test, y_pred))
    st.text(classification_report(y_test, y_pred))

# Sidebar - Manual prediction
st.sidebar.subheader("🎯 Try Manual Prediction")
user_input = {}
for col in X.columns:
    if df[col].dtype == "object":
        options = df[col].unique().tolist()
        user_input[col] = st.sidebar.selectbox(col, options)
    else:
        user_input[col] = st.sidebar.number_input(col, float(df[col].min()), float(df[col].max()), float(df[col].mean()))

# Encode manual input
input_df = pd.DataFrame([user_input])
for col in input_df.columns:
    if col in label_encoders:
        input_df[col] = label_encoders[col].transform(input_df[col])

pred = model.predict(input_df)[0]
pred_label = "Diabetic" if pred == 1 else "Non-Diabetic"
st.sidebar.success(f"Prediction: **{pred_label}**")

# =======================
# 📊 Visualizations
# =======================
st.header("📈 Visual Explorations")

# 1. Diabetes count
st.subheader("Diabetes Count")
fig1, ax1 = plt.subplots()
sns.countplot(x='diabetes', data=df, ax=ax1)
st.pyplot(fig1)

# 2. Age Distribution
st.subheader("Age Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(df["age"], kde=True, color="teal", ax=ax2)
st.pyplot(fig2)

# 3. Correlation heatmap
st.subheader("Correlation Heatmap")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.heatmap(df_encoded.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax3)
st.pyplot(fig3)
