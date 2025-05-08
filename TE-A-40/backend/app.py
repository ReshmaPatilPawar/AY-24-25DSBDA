from flask import Flask, request, jsonify, send_from_directory
import pickle
import numpy as np
import os

app = Flask(__name__, static_folder='../frontend')

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)

        required_fields = ['Store_ID', 'Product_ID', 'Promotion', 'Holiday', 'Day', 'Month', 'Year']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        input_features = np.array([
            data['Store_ID'],
            data['Product_ID'],
            data['Promotion'],
            data['Holiday'],
            data['Day'],
            data['Month'],
            data['Year']
        ]).reshape(1, -1)

        prediction = model.predict(input_features)
        predicted_sales = int(prediction[0])

        # 🔥 Return number only (not a string)
        return jsonify({'predicted_sales': predicted_sales})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
