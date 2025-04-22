import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

# Initialize Flask app
app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load label encoders
with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

# Load scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def encode_input(data):
    """
    Encodes categorical values using the saved encoders, handling unseen labels,
    and scales numerical features.

    Expected order of features:
    0: Platform (categorical)
    1: Year (numeric)
    2: Genre (categorical)
    3: Publisher (categorical)
    4: NA_Sales (numeric)
    5: EU_Sales (numeric)
    6: JP_Sales (numeric)
    7: Other_Sales (numeric)
    """

    # Categorical feature indices
    categorical_indices = {0: "Platform", 2: "Genre", 3: "Publisher"}

    # Encode categorical features
    for idx, col in categorical_indices.items():
        if data[idx] not in label_encoders[col].classes_:
            # If unseen label, replace with 'Unknown' or add dynamically
            data[idx] = "Unknown"
        
        # Convert category to numerical encoding
        data[idx] = label_encoders[col].transform([data[idx]])[0]

    # Convert numeric features to float
    numeric_indices = [1, 4, 5, 6, 7]
    for idx in numeric_indices:
        data[idx] = float(data[idx])

    # Convert to numpy array, reshape for model input, and scale
    data = np.array(data).reshape(1, -1)
    data = scaler.transform(data)

    return data

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = data["features"]

        # Encode and scale the input features
        features = encode_input(features)

        # Predict global sales
        prediction = model.predict(features)[0]

        return jsonify({"predicted_global_sales": round(float(prediction), 2)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
