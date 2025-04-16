from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

# Load model
model = joblib.load('model.pkl')

# Optional: test route to confirm server is running
@app.route('/')
def home():
    return '⚡ Electricity Consumption Prediction API is running!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array([[ 
            data['Temperature'],
            data['Humidity'],
            data['WindSpeed'],
            data['GeneralDiffuseFlows'],
            data['DiffuseFlows'],
            data['Hour'],
            data['Day'],
            data['Month']
        ]])

        prediction = model.predict(features)[0].tolist()

        return jsonify({
            'PowerConsumption_Zone1': prediction[0],
            'PowerConsumption_Zone2': prediction[1],
            'PowerConsumption_Zone3': prediction[2]
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
