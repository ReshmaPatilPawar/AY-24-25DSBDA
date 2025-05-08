from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return '🚀 EV Charging Station Predictor API is running!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [data['population_density'], data['traffic_density'], data['ev_count'],
                data['distance_from_nearest_station']]
    prediction = model.predict([features])[0]
    return jsonify({'recommendation': 'Yes' if prediction == 1 else 'No'})


if __name__ == '__main__':
    app.run(debug=True)
