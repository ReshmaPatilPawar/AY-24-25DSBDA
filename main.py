from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import traceback

app = Flask(__name__)
CORS(app)

# Load model and encoders
with open("placement_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        # Convert all fields to correct numeric types
        processed_data = {
            'CGPA': float(data.get('CGPA', 0)),
            'Internships': int(data.get('Internships', 0)),
            'Projects': int(data.get('Projects', 0)),
            'Workshops/Certifications': int(data.get('Workshops/Certifications', 0)),
            'AptitudeTestScore': float(data.get('AptitudeTestScore', 0)),
            'SoftSkillsRating': float(data.get('SoftSkillsRating', 0)),
            'ExtracurricularActivities': int(data.get('ExtracurricularActivities', 0)),
            'PlacementTraining': int(data.get('PlacementTraining', 0)),
            'SSC_Marks': float(data.get('SSC_Marks', 0)),
            'HSC_Marks': float(data.get('HSC_Marks', 0))
        }

        input_df = pd.DataFrame([processed_data])

        prediction = model.predict(input_df)[0]
        proba = model.predict_proba(input_df)[0][1]

        # Rescale probability
        min_proba = 0.78
        max_proba = 0.85
        scaled_proba = min_proba + (max_proba - min_proba) * proba
        scaled_proba_percent = round(scaled_proba * 100, 2)

        label_decoder = encoders["PlacementStatus"]
        prediction_label = label_decoder.inverse_transform([prediction])[0]

        strengths = []
        if processed_data["AptitudeTestScore"] > 70:
            strengths.append("Strong aptitude")
        if processed_data["SoftSkillsRating"] > 3.5:
            strengths.append("Excellent soft skills")
        if processed_data["PlacementTraining"] == 1:
            strengths.append("Placement training attended")
        if not strengths:
            strengths.append("No major strengths detected")

        if scaled_proba_percent >= 75:
            verdict = "🎉 High chance of placement! Strong profile."
        elif scaled_proba_percent >= 55:
            verdict = "⚖️ Moderate chance. Profile is average — improvements needed."
        else:
            verdict = "⚠️ Low chance. Recommend skill-building & certifications."

        return jsonify({
            "prediction": prediction_label,
            "probability": scaled_proba_percent,
            "strengths": strengths,
            "verdict": verdict
        })

    except Exception as e:
        traceback.print_exc()  # See full traceback in terminal
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
