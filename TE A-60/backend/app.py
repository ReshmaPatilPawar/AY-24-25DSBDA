from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Get the absolute path to the model files
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
model_path = os.path.join(base_dir, 'model.pkl')
columns_path = os.path.join(base_dir, 'model_columns.pkl')

# Load the model and column list
model = joblib.load(model_path)
model_columns = joblib.load(columns_path)

@app.route('/')
def home():
    return "🚀 Air Pollution Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        input_df = pd.DataFrame([data])

        # Reindex the DataFrame to match the model's expected input
        input_df = input_df.reindex(columns=model_columns, fill_value=0)

        prediction = model.predict(input_df)[0]
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
