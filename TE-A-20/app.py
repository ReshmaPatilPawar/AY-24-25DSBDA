from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import os
import joblib
app = Flask(__name__)
import pandas as pd


model = joblib.load('gradient_boosting_model.pkl')
scaler = joblib.load('scaler.pkl')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received JSON:", data)  # Log data

        # Extract values
        study_time = data.get('StudyTimeWeekly', 0)
        absences = data.get('AbsencesPercentage', 0)
        tutoring = 1 if data.get('Tutoring', 'No') == 'Yes' else 0
        extracurricular = 1 if data.get('Extracurricular', 'No') == 'Yes' else 0
        volunteering = 1 if data.get('Volunteering', 'No') == 'Yes' else 0

        # Interaction terms
        study_time_absences = study_time * absences
        study_time_volunteering = study_time * volunteering
        extracurricular_volunteering = extracurricular * volunteering

        # DataFrame for prediction
        input_df = pd.DataFrame([{
            'StudyTimeWeekly': study_time,
            'AbsencesPercentage': absences,
            'Tutoring': tutoring,
            'Extracurricular': extracurricular,
            'Volunteering': volunteering,
            'StudyTimeAbsences': study_time_absences,
            'StudyTimeVolunteering': study_time_volunteering,
            'ExtracurricularVolunteering': extracurricular_volunteering
        }])

        print("Input DataFrame:", input_df)

        # Scale and predict
        scaled_features = scaler.transform(input_df)
        predicted_gpa = model.predict(scaled_features)[0]

        return jsonify({'predicted_gpa': round(predicted_gpa, 2)})

    except Exception as e:
        print(f"Error in /predict route: {e}")  # Print detailed error
        return jsonify({'error': str(e)}), 500



