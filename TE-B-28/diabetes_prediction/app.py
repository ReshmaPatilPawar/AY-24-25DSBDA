# Import necessary libraries
from flask import Flask, render_template, request
import pickle
import os
import numpy as np

# Create a Flask app
app = Flask(__name__)

# Load the trained model and scaler from files
MODEL_PATH = os.path.join(os.path.dirname(__file__), "diabetes_model.pkl")
SCALER_PATH = os.path.join(os.path.dirname(__file__), "scaler.pkl")

# Open and load the model
model = pickle.load(open(MODEL_PATH, "rb"))

# Open and load the scaler
scaler = pickle.load(open(SCALER_PATH, "rb"))

# Route for the homepage
@app.route('/')
def home():
    # Show the input form to the user
    return render_template('index.html')

# Route for handling the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get gender input from the form
    gender = request.form.get('gender')
    
    try:
        # If gender is Female, use the input for Pregnancies; else set it to 0
        pregnancies = float(request.form.get('Pregnancies', 0)) if gender == 'Female' else 0.0

        # Get the rest of the form inputs and convert them to float
        glucose = float(request.form['Glucose'])
        bp = float(request.form['BloodPressure'])
        skin = float(request.form['SkinThickness'])
        insulin = float(request.form['Insulin'])
        bmi = float(request.form['BMI'])
        dpf = float(request.form['DiabetesPedigreeFunction'])
        age = float(request.form['Age'])

        # Make a list of all input features
        input_features = [pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]

        # Scale the features using the loaded scaler
        input_scaled = scaler.transform([input_features])

        # Predict probability using the trained model
        proba = model.predict_proba(input_scaled)[0][1]

        # If probability is 50% or more, predict 'Yes'; else 'No'
        result = 'Yes' if proba >= 0.5 else 'No'

        # Show result and probability on the webpage
        return render_template('index.html', result=result, gender=gender, proba=round(proba*100, 2))

    except Exception as e:
        # If there's any error (like wrong input), show error message
        return render_template('index.html', error=str(e))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
