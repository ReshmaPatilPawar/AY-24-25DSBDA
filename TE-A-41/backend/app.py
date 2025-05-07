from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model
model = joblib.load('model/imdb_model.pkl')
@app.route('/')
def home():
    return "🎬 IMDb Rating Predictor API is running!"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({'predicted_rating': round(prediction, 2)})

if __name__ == '__main__':
    app.run(debug=True)
