from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model and scaler
model = None
scaler = None
feature_names = None

def load_model_and_scaler():
    global model, scaler, feature_names
    if not os.path.exists('fraud_model.pkl') or not os.path.exists('scaler.pkl'):
        return False
    
    model = joblib.load('fraud_model.pkl')
    scaler = joblib.load('scaler.pkl')
    
    with open('feature_names.txt', 'r') as f:
        feature_names = f.read().split(',')
    
    return True

@app.route('/api/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return jsonify({'error': 'Model not loaded. Run train_model.py first.'}), 500
    
    # Get the transaction data from the request
    data = request.json
    
    # Check if all features are present
    for feature in feature_names:
        if feature not in data:
            return jsonify({'error': f'Missing feature: {feature}'}), 400
    
    # Prepare input for prediction
    input_data = np.array([data[feature] for feature in feature_names]).reshape(1, -1)
    
    # Scale the input
    scaled_input = scaler.transform(input_data)
    
    # Make prediction
    prediction = int(model.predict(scaled_input)[0])
    probability = float(model.predict_proba(scaled_input)[0][1])  # Probability of fraud
    
    # Prepare explanation
    explanation = []
    if probability > 0.3:
        if data['amount'] > 200:
            explanation.append(f"Transaction amount (${data['amount']:.2f}) is higher than typical")
        if abs(data['v1']) > 2:
            explanation.append("Unusual pattern detected in transaction characteristics (v1)")
        if abs(data['v3']) > 2:
            explanation.append("Unusual pattern detected in transaction characteristics (v3)")
    
    # Prepare response
    response = {
        'prediction': prediction,
        'probability': probability,
        'isFraud': prediction == 1,
        'explanation': explanation
    }
    
    return jsonify(response)

@app.route('/api/example-values', methods=['GET'])
def example_values():
    legitimate = {
        'amount': 75.5, 
        'time': 12.5, 
        'v1': 0.5, 
        'v2': 0.2, 
        'v3': 0.1, 
        'v4': -0.5, 
        'v5': 0.3
    }
    
    fraudulent = {
        'amount': 350.75, 
        'time': 3.25, 
        'v1': -2.5, 
        'v2': 0.2, 
        'v3': 2.5, 
        'v4': -0.5, 
        'v5': 0.3
    }
    
    return jsonify({
        'legitimate': legitimate,
        'fraudulent': fraudulent
    })

@app.route('/api/features', methods=['GET'])
def get_features():
    if feature_names is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    return jsonify({'features': feature_names})

if __name__ == '__main__':
    if load_model_and_scaler():
        print("Model loaded successfully!")
    else:
        print("Error: Model or scaler files not found. Run train_model.py first.")
    
    app.run(debug=True) 