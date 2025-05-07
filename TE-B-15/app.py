from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

# Hardcode feature values (update these based on your dataset)
hardcoded_features = [0, 0, 0, 0, 0,  # symboling, normalized_losses, etc.
                      0,  # num_doors
                      0,  # body_style
                      0,  # drive_wheels
                      0,  # engine_location
                      0,  # wheel_base
                      0,  # length
                      0,  # width
                      0,  # height
                      0,  # curb_weight
                      0,  # engine_type
                      0,  # num_cylinders
                      0,  # engine_size
                      0,  # fuel_system
                      0,  # bore
                      0,  # stroke
                      0,  # compression_ratio
                      0,  # horsepower
                      0,  # peak_rpm
                      0,  # city_mpg
                      0]  # highway_mpg

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs (5 inputs only)
        features = [float(request.form[f'feature{i}']) for i in range(1, 6)]
        
        # Combine hardcoded features with user input
        final_input = np.array([features + hardcoded_features[5:]])

        # Make prediction
        prediction = model.predict(final_input)[0]
        return render_template('index.html', prediction_text=f"Predicted Price: ${prediction:,.2f}")
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
