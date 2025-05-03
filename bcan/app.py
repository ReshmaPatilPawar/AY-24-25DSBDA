from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
with open("cancer_model.pkl", "rb") as f:
    model = pickle.load(f)

# User inputs
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect 6 key inputs from the user
        radius = float(request.form['radius_mean'])
        texture = float(request.form['texture_mean'])
        perimeter = float(request.form['perimeter_mean'])
        area = float(request.form['area_mean'])
        concavity = float(request.form['concavity_mean'])
        concave_points = float(request.form['concave_points_mean'])

        # Use dataset mean values for all 30 features
        default_values = [  # From Cancer.csv
            14.127, 19.289, 91.969, 654.889, 0.096, 0.104, 0.089, 0.049, 0.181, 0.062,
            0.405, 1.216, 2.867, 40.337, 0.007, 0.025, 0.031, 0.012, 0.020, 0.004,
            16.269, 25.677, 107.261, 880.583, 0.132, 0.254, 0.273, 0.115, 0.291, 0.084
        ]

        # Inject user values in correct positions
        default_values[0] = radius
        default_values[1] = texture
        default_values[2] = perimeter
        default_values[3] = area
        default_values[6] = concavity
        default_values[7] = concave_points

        # Predict using aligned input
        prediction = model.predict([default_values])[0]
        result = "Malignant" if prediction == 1 else "Benign"
        
        return render_template("index.html", prediction_text=f"Predicted Diagnosis: {result}")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get the port from the environment variable
    app.run(host="0.0.0.0", port=port, debug=True)
