import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib  # For saving/loading model

# Must be the first Streamlit command
st.set_page_config(page_title="Email Spam Detector", layout="centered")

# Check if the model is already saved, else train a new model
model_filename = 'spam_model.pkl'
model = None
df = None

st.title("📧 Email Spam Detection")
st.write("Enter an email message to check if it's spam or not.")

# Reload button
if st.button("Reload Model"):
    try:
        # Load dataset
        df = pd.read_csv('C:/Users/vchin/OneDrive/Desktop/Email_Detection_System/data/spam.csv', encoding='ISO-8859-1')
        df = df.rename(columns={"v1": "Category", "v2": "Message"})
        df = df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'])
        df['Spam'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)

        X = df['Message']
        y = df['Spam']

        # Train a pipeline (text vectorizer + Naive Bayes)
        model = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('nb', MultinomialNB())
        ])

        # Fit the model
        model.fit(X, y)

        # Save the model to disk
        joblib.dump(model, model_filename)
        st.success("Model successfully trained and saved!")
    except Exception as e:
        st.error(f"Error training or saving model: {e}")
else:
    try:
        # Load pre-trained model if it exists
        model = joblib.load(model_filename)
        # Also load data for accuracy/confusion matrix (optional)
        df = pd.read_csv('C:/Users/vchin/OneDrive/Desktop/Email_Detection_System/data/spam.csv', encoding='ISO-8859-1')
        df = df.rename(columns={"v1": "Category", "v2": "Message"})
        df = df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'])
        df['Spam'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)
    except FileNotFoundError:
        st.error("Model file not found. Please train and save the model first.")

# Text input from user
email_input = st.text_area("Your Email Message", height=150)

# Clear the input text
if st.button("Clear Input"):
    email_input = ""

# Only make predictions if model is loaded and input text is provided
if model and st.button("Detect"):
    if email_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Detecting..."):
            prediction = model.predict([email_input])[0]

        if prediction == 1:
            st.error("🚨 This is a **Spam Email**!")
        else:
            st.success("✅ This is a **Ham Email**!")

        # Additional evaluation (optional)
        if df is not None:
            y_pred = model.predict(df['Message'])
            accuracy = accuracy_score(df['Spam'], y_pred)
            cm = confusion_matrix(df['Spam'], y_pred)

            # Show accuracy and confusion matrix
            st.markdown(f"### Model Accuracy: {accuracy*100:.2f}%")
            st.markdown("### Confusion Matrix:")
            st.write(cm)

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit & scikit-learn")
