# backend/main.py
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model from subdirectory
model = joblib.load("model/car_price_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        return jsonify({'predicted_price': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
