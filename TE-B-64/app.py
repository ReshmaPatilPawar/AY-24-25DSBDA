from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os
import sys

# Add the project root to the Python path to import the model training module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.models.model_training import train_model

app = Flask(__name__)
# Enable CORS with simple settings
CORS(app)

# Check if model exists, if not train it
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models/diabetes_model.pkl')
scaler_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models/scaler.pkl')

print(f"Current working directory: {os.getcwd()}")
print(f"Checking for model at: {model_path}")

try:
    # Try to load the model and scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    print("Model and scaler loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    # Train a new model if loading fails
    print("Training new model...")
    if not os.path.exists(os.path.dirname(model_path)):
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
    train_model()
    # Try loading again
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

@app.route('/')
def home():
    return jsonify({"message": "Diabetes Prediction API is running!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Received prediction request")
        data = request.json
        print(f"Request data: {data}")
        
        # Extract features from the request
        features = pd.DataFrame({
            'Pregnancies': [float(data.get('pregnancies', 0))],
            'Glucose': [float(data.get('glucose', 0))],
            'BloodPressure': [float(data.get('bloodPressure', 0))],
            'SkinThickness': [float(data.get('skinThickness', 0))],
            'Insulin': [float(data.get('insulin', 0))],
            'BMI': [float(data.get('bmi', 0))],
            'DiabetesPedigreeFunction': [float(data.get('diabetesPedigreeFunction', 0))],
            'Age': [float(data.get('age', 0))]
        })
        
        # Scale the features
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0][1]
        
        response = {
            'prediction': int(prediction),
            'probability': float(probability),
            'message': 'Diabetes detected' if prediction == 1 else 'No diabetes detected'
        }
        print(f"Prediction response: {response}")
        
        return jsonify(response)
    
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

# Vercel serverless function handler
def handle_request(req):
    with app.request_context(req):
        return app.full_dispatch_request()

# For local development
if __name__ == '__main__':
    print(f"Starting Flask server on port 8000...")
    app.run(debug=True, host='0.0.0.0', port=8000) 