from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)

# Enable CORS
CORS(app)

# Load models and label encoders
classifier = joblib.load("classifier.pkl")
regressor = joblib.load("regressor.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Home route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route: accepts form data and returns predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from the form
        input_data = {
            'Age': int(request.form['age']),
            'Gender': request.form['gender'],
            'Item Purchased': request.form['item'],
            'Category': request.form['category'],
            'Location': request.form['location'],
            'Size': request.form['size'],
            'Color': request.form['color'],
            'Season': request.form['season'],
            'Review Rating': float(request.form['rating']),
            'Subscription Status': request.form['subscribed'],
            'Payment Method': request.form['paymentMethod'],
            'Shipping Type': request.form['shippingType'],
            'Promo Code Used': request.form['promoCode'],
            'Previous Purchases': int(request.form['previousPurchases']),
            'Preferred Payment Method': request.form['preferredPayment'],
            'Frequency of Purchases': request.form['frequency']
        }

        # Encode categorical data using pre-loaded label encoders
        for key in input_data:
            if key in label_encoders:
                le = label_encoders[key]
                try:
                    input_data[key] = le.transform([input_data[key]])[0]
                except ValueError:
                    # Handle unseen labels by assigning a default label or skipping
                    print(f"Warning: Unseen label '{input_data[key]}' encountered for '{key}', assigning default value.")
                    input_data[key] = le.transform([le.classes_[0]])[0]  # Default to the first class

        # Create input array for prediction
        input_array = np.array(list(input_data.values())).reshape(1, -1)

        # Make predictions
        discount_prediction = classifier.predict(input_array)[0]
        purchase_prediction = regressor.predict(input_array)[0]

        # Decode the classifier output back to its original label
        discount_label = label_encoders['Discount Applied'].inverse_transform([discount_prediction])[0]

        return jsonify({
            'discount_prediction': discount_label,
            'purchase_prediction': round(purchase_prediction, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
