from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the model
MODEL_PATH = 'models/thyroid_model.pkl'
SCALER_PATH = 'models/scaler.pkl'

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Check if model exists, if not create a simple example model
if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
    # This is a placeholder model for demonstration
    from sklearn.ensemble import RandomForestClassifier
    # Example features and labels
    X = np.random.rand(100, 5)  # 5 features: age, TSH, T3, T4, gender
    y = np.random.randint(0, 3, 100)  # 3 classes: normal, hypothyroidism, hyperthyroidism
    
    # Create and save a simple model
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_scaled, y)
    
    # Save model and scaler
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    with open(SCALER_PATH, 'wb') as f:
        pickle.dump(scaler, f)
        
# Load the model and scaler
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)
with open(SCALER_PATH, 'rb') as f:
    scaler = pickle.load(f)

# Class labels for interpretation
CLASS_LABELS = {
    0: "Normal Thyroid Function",
    1: "Hypothyroidism (Underactive Thyroid)",
    2: "Hyperthyroidism (Overactive Thyroid)"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get data from form
            age = float(request.form['age'])
            tsh = float(request.form['tsh'])
            t3 = float(request.form['t3'])
            t4 = float(request.form['t4'])
            gender = 1 if request.form['gender'] == 'male' else 0
            
            # Prepare data for prediction
            input_data = np.array([[age, tsh, t3, t4, gender]])
            input_data_scaled = scaler.transform(input_data)
            
            # Make prediction
            prediction = model.predict(input_data_scaled)[0]
            prediction_proba = model.predict_proba(input_data_scaled)[0]
            
            # Prepare result
            result = {
                'prediction': CLASS_LABELS[prediction],
                'confidence': round(np.max(prediction_proba) * 100, 2),
                'probabilities': {
                    CLASS_LABELS[i]: round(prediction_proba[i] * 100, 2) 
                    for i in range(len(CLASS_LABELS))
                }
            }
            
            return render_template('result.html', result=result)
        
        except Exception as e:
            return render_template('error.html', error=str(e))
    
    return render_template('predict.html')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.get_json()
        
        # Get data from JSON
        age = float(data['age'])
        tsh = float(data['tsh'])
        t3 = float(data['t3'])
        t4 = float(data['t4'])
        gender = 1 if data['gender'] == 'male' else 0
        
        # Prepare data for prediction
        input_data = np.array([[age, tsh, t3, t4, gender]])
        input_data_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_data_scaled)[0]
        prediction_proba = model.predict_proba(input_data_scaled)[0]
        
        # Prepare result
        result = {
            'prediction': CLASS_LABELS[prediction],
            'confidence': round(np.max(prediction_proba) * 100, 2),
            'probabilities': {
                CLASS_LABELS[i]: round(prediction_proba[i] * 100, 2) 
                for i in range(len(CLASS_LABELS))
            }
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)