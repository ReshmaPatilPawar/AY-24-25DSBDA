
from flask import Flask, request, render_template
import joblib
import pandas as pd
import numpy as np
from pyngrok import ngrok

app = Flask(__name__)

# Load model artifacts
model = joblib.load('churn_model.pkl')
scaler = joblib.load('scaler.pkl')
feature_columns = joblib.load('feature_columns.pkl')
label_encoders = joblib.load('label_encoders.pkl')
optimal_threshold = joblib.load('optimal_threshold.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Create mapping dictionaries for categorical features
        contract_map = {'month-to-month': 0, 'one year': 1, 'two year': 2}
        internet_map = {'DSL': 0, 'Fiber optic': 1, 'No': 2}
        payment_map = {
            'Electronic check': 0,
            'Mailed check': 1,
            'Bank transfer': 2,
            'Credit card': 3
        }

        # Create dictionary with all features initialized to 0
        input_data = {col: 0 for col in feature_columns}

        # Set values from form
        input_data['tenure'] = float(request.form['tenure'])
        input_data['MonthlyCharges'] = float(request.form['monthlycharges'])
        input_data['TotalCharges'] = float(request.form['totalcharges'])
        input_data['SeniorCitizen'] = int(request.form['seniorcitizen'])

        # Handle categorical features
        input_data['Contract'] = contract_map[request.form['contract']]
        input_data['InternetService'] = internet_map[request.form['internetservice']]
        input_data['PaymentMethod'] = payment_map[request.form['paymentmethod']]
        input_data['OnlineSecurity'] = int(request.form['onlinesecurity'])
        input_data['TechSupport'] = int(request.form['techsupport'])

        # Create DataFrame with all features in correct order
        input_df = pd.DataFrame([input_data])[feature_columns]

        # Scale the input
        input_scaled = scaler.transform(input_df)

        # Make prediction
        probability = model.predict_proba(input_scaled)[0][1]
        result = 'Churn' if probability >= optimal_threshold else 'No Churn'

        # Prepare data for visualization
        churn_prob = round(probability * 100, 1)
        no_churn_prob = round((1 - probability) * 100, 1)

        return render_template('index.html',
                            prediction=result,
                            churn_prob=churn_prob,
                            no_churn_prob=no_churn_prob,
                            probability=f"{probability:.4f}")

    except Exception as e:
        print("Error:", e)
        return render_template('index.html',
                            prediction="Error during prediction",
                            error=str(e))

if __name__ == '__main__':
    # Set up ngrok
    public_url = ngrok.connect(5000)
    print(" * Public URL:", public_url)
    app.run(host='0.0.0.0', port=5000)
