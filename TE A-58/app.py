import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('train_model.pkl')
scaler = joblib.load('scaler.pkl')

# App title and layout
st.set_page_config(page_title="Lung Cancer Prediction", layout="centered")

st.title("🩺 Lung Cancer Risk Prediction")
st.write("Please fill in the following health-related inputs to predict your lung cancer risk.")

with st.form("prediction_form"):
    age = st.slider("Age", 20, 100, 40)
    gender = st.selectbox("Gender", ["Male", "Female"])
    air_pollution = st.slider("Air Pollution", 1, 10, 5)
    alcohol_use = st.slider("Alcohol Use", 1, 10, 5)
    dust_allergy = st.slider("Dust Allergy", 1, 10, 5)
    occupational_hazards = st.slider("Occupational Hazards", 1, 10, 5)
    genetic_risk = st.slider("Genetic Risk", 1, 10, 5)
    chronic_lung_disease = st.slider("Chronic Lung Disease", 1, 10, 5)
    balanced_diet = st.slider("Balanced Diet", 1, 10, 5)
    obesity = st.slider("Obesity", 1, 10, 5)
    smoking = st.slider("Smoking", 1, 10, 5)
    passive_smoker = st.slider("Passive Smoker", 1, 10, 5)
    chest_pain = st.slider("Chest Pain", 1, 10, 5)
    coughing_blood = st.slider("Coughing of Blood", 1, 10, 5)
    fatigue = st.slider("Fatigue", 1, 10, 5)
    weight_loss = st.slider("Weight Loss", 1, 10, 5)
    shortness_of_breath = st.slider("Shortness of Breath", 1, 10, 5)
    wheezing = st.slider("Wheezing", 1, 10, 5)
    swallowing_difficulty = st.slider("Swallowing Difficulty", 1, 10, 5)
    clubbing = st.slider("Clubbing of Finger Nails", 1, 10, 5)
    frequent_cold = st.slider("Frequent Cold", 1, 10, 5)
    dry_cough = st.slider("Dry Cough", 1, 10, 5)
    snoring = st.slider("Snoring", 1, 10, 5)

    submit = st.form_submit_button("🔍 Predict")

if submit:
    gender_val = 1 if gender == "Male" else 0

    # ✅ FIXED: Closing brackets issue
    features = np.array([[
        age, gender_val, air_pollution, alcohol_use, dust_allergy,
        occupational_hazards, genetic_risk, chronic_lung_disease,
        balanced_diet, obesity, smoking, passive_smoker, chest_pain,
        coughing_blood, fatigue, weight_loss, shortness_of_breath,
        wheezing, swallowing_difficulty, clubbing, frequent_cold,
        dry_cough, snoring
    ]])

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)

    st.markdown("---")
    st.subheader("🧾 Prediction Result")

    if prediction[0] == 1:
        st.error("⚠️ High risk of Lung Cancer detected. Please consult a medical professional.")
    else:
        st.success("✅ Low risk of Lung Cancer detected. Keep maintaining a healthy lifestyle.")
