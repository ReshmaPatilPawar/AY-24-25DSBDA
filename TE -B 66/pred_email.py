import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

st.set_page_config(page_title="Spam Classifier", page_icon="📧", layout="centered")

# Load and clean the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("email.csv")

    # Drop rows with missing values in essential columns
    df = df.dropna(subset=["Category", "Message"])

    # Map ham/spam to 0/1
    df["Category"] = df["Category"].map({"ham": 0, "spam": 1})

    # Drop any rows where mapping failed (i.e., unknown labels → NaN)
    df = df.dropna(subset=["Category"])

    # Ensure the label is of integer type
    df["Category"] = df["Category"].astype(int)

    return df

# Load the dataset
df = load_data()

# Split features and labels
X = df["Message"]
y = df["Category"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Text vectorization
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Streamlit UI
st.markdown("<h1 style='text-align: center;'>📧 Email Spam Classifier</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Choose Action",
    ["📊 Show Dataset", "🔍 Predict Message", "📈 Evaluate Model"]
)

# Show first 10 records
if menu == "📊 Show Dataset":
    st.subheader("📄 First 10 Records from the Dataset")
    st.dataframe(df.head(10), use_container_width=True)
    st.toast("Here are your first 10 emails 📩")

# Predict Message
elif menu == "🔍 Predict Message":
    st.subheader("🧠 Type a Message to Predict Spam or Not")
    user_input = st.text_area("✏️ Enter the message:")

    if st.button("Predict", use_container_width=True):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter a message to analyze.")
        else:
            input_vec = vectorizer.transform([user_input])
            prediction = model.predict(input_vec)[0]
            label = "🚫 Spam" if prediction == 1 else "✅ Ham"
            st.success(f"📌 Prediction: {label}")
            st.balloons()

# Evaluate Model
elif menu == "📈 Evaluate Model":
    st.subheader("📊 Evaluation on Test Dataset")
    y_pred = model.predict(X_test_vec)

    accuracy = accuracy_score(y_test, y_pred)
    st.metric(label="✅ Accuracy", value=f"{accuracy*100:.2f}%")

    with st.expander("📄 View Classification Report"):
        st.text(classification_report(y_test, y_pred, target_names=["Ham", "Spam"]))

    st.toast("Model evaluation complete 🧪")
