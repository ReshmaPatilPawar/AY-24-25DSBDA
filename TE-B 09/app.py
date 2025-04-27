# from flask import Flask, request, jsonify
# import joblib
# import numpy as np

# # Load the trained model
# model = joblib.load("diabetes_model.pkl")  # Ensure this file is in the same folder

# # Initialize Flask app
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Diabetes Prediction API is running!"

# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         # Get JSON data from the request
#         data = request.get_json()
#         features = np.array(data["features"]).reshape(1, -1)  # Ensure it's a 2D array

#         # Make prediction
#         prediction = model.predict(features)[0]
#         result = "Diabetic" if prediction == 1 else "Non-Diabetic"

#         return jsonify({"prediction": result})

#     except Exception as e:
#         return jsonify({"error": str(e)})

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS  # Add this

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = joblib.load("diabetes_model.pkl")

@app.route("/")
def home():
    return "Diabetes Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)  
        prediction = model.predict(features)[0]
        result = "Diabetic" if prediction == 1 else "Non-Diabetic"
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
