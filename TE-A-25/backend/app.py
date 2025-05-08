from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # ✅ enable CORS for all routes

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = [
        int(data['online_order']),
        int(data['book_table']),
        int(data['location']),
        int(data['rest_type']),
        int(data['cuisines']),
        int(data['cost']),
        int(data['listed_in']),
        int(data['votes'])
    ]
    prediction = model.predict([features])[0]
    return jsonify({'predicted_rating': round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)

