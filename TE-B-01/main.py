from flask import Flask, request, jsonify
import pandas as pd
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Load Models (removed Random Forest)
model_paths = {
    "Linear Regression": r"C:\Users\saura\OneDrive\Desktop\DSProject\wp\linear_regression\model.pkl",
    "XGBoost": r"C:\Users\saura\OneDrive\Desktop\DSProject\wp\xgboost\model.pkl"
}

try:
    models = {name: joblib.load(path) for name, path in model_paths.items()}
    print("✅ Models loaded successfully!")
except Exception as e:
    print(f"❌ Error loading models: {e}")

# Load dataset to get feature names
file_path = r"C:\Users\saura\OneDrive\Desktop\DSProject\wp\pune.csv"
try:
    df = pd.read_csv(file_path)
    df['date_time'] = pd.to_datetime(df['date_time'])
    df['year'], df['month'], df['day'] = df['date_time'].dt.year, df['date_time'].dt.month, df['date_time'].dt.day
    df.drop(columns=['date_time', 'moonrise', 'moonset', 'sunrise', 'sunset', 'location'], inplace=True)
    feature_columns = df.drop(columns=["maxtempC", "mintempC", "windspeedKmph", "humidity", "precipMM"]).columns
    print("✅ Dataset loaded successfully!")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        print("Received data:", data)  # Debugging

        year, month, day = int(data['year']), int(data['month']), int(data['day'])

        # Create input data
        input_data = pd.DataFrame(columns=feature_columns)
        input_data.loc[0] = [None] * len(feature_columns)
        input_data["year"], input_data["month"], input_data["day"] = year, month, day

        # Fix FutureWarning
        input_data = input_data.infer_objects(copy=False)
        input_data.fillna(df.mean(numeric_only=True), inplace=True)

        predictions = {}
        for name, model in models.items():
            try:
                print(f"Predicting with {name}...")
                pred = model.predict(input_data)
                print(f"Raw prediction output ({name}):", pred)

                # Convert predictions to standard Python float
                pred = pred.astype(float)  # Convert NumPy float32 → Python float

                predictions[name] = {
                    "max_temp": round(pred[0][0], 2),
                    "min_temp": round(pred[0][1], 2),
                    "wind_speed": round(pred[0][2], 2),
                    "humidity": round(pred[0][3], 2),
                    "precipitation": max(round(pred[0][4], 2), 0)
                }
            except Exception as e:
                print(f"Error predicting with {name}: {e}")
                predictions[name] = {"error": str(e)}

        return jsonify(predictions)

    except Exception as e:
        print("❌ Server error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
