from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

# Load the trained model
model = joblib.load('loan_approval_model_optimized.pkl')

# Route: Home
@app.route('/')
def home():
    return render_template('index.html')

# Route: Predict from HTML Form
@app.route('/predict_form', methods=['POST'])
def predict_form():
    try:
        data = request.form

        # Extract features
        features = [
            int(data['Gender']), int(data['Married']), int(data['Dependents']), int(data['Education']),
            int(data['Self_Employed']), int(data['ApplicantIncome']), int(data['CoapplicantIncome']),
            int(data['LoanAmount']), int(data['Loan_Amount_Term']), int(data['Credit_History']), int(data['Property_Area'])
        ]

        # Make prediction and calculate confidence
        prediction = model.predict([features])[0]
        proba = model.predict_proba([features])[0]
        confidence = round(max(proba) * 100, 2)

        # Create result message
        prediction_text = 'Approved' if prediction == 1 else 'Rejected'
        result = f"{prediction_text} ({confidence}% confidence)"

        return render_template('index.html', prediction=result)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

