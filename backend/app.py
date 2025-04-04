from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import warnings
import os

warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'backend', 'templates'))

# Load the trained model
model = pickle.load(open('backend/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        features = [float(request.form.get(feature)) for feature in [
            'lotsize', 'bedrooms', 'bathrms', 'stories', 
            'driveway', 'recroom', 'fullbase', 'gashw', 
            'airco', 'garagepl', 'prefarea'
        ]]

        # Convert to numpy array and predict
        features = np.array([features])
        prediction = model.predict(features)

        # Return the predicted price as JSON
        return jsonify({'predicted_price': round(prediction[0], 2)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
