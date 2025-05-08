from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows requests from Postman or frontend

# Load the trained model
model = joblib.load('random_forest_addiction_model.pkl')  # Make sure file is correctly named

@app.route('/')
def home():
    return jsonify({"message": "📱 Phone Addiction Prediction API is up and running!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)

        # Validate keys
        required_keys = ['screen_time', 'gaming_time', 'social_media_time', 'data_usage']
        if not all(key in data for key in required_keys):
            return jsonify({"error": "Missing one or more required fields."}), 400

        # Extract & convert features
        screen_time = float(data['screen_time'])
        gaming_time = float(data['gaming_time'])
        social_media_time = float(data['social_media_time'])
        data_usage = float(data['data_usage'])

        # Create input array
        input_data = np.array([[screen_time, gaming_time, social_media_time, data_usage]])
        prediction = model.predict(input_data)[0]

        result = "Addicted" if prediction == 1 else "Not Addicted"
        return jsonify({
            # "screen_time": screen_time,
            # "gaming_time": gaming_time,
            # "social_media_time": social_media_time,
            # "data_usage": data_usage,
            "prediction": int(prediction),
            "result": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
