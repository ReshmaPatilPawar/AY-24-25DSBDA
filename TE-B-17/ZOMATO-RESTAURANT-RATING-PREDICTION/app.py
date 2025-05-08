from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get 8 form values
        votes = float(request.form['votes'])  # Assuming votes is a numeric field
        cost = float(request.form['cost'])  # Assuming cost is a numeric field
        online_order = int(request.form['online_order'])  # Online order (0 or 1)
        book_table = int(request.form['book_table'])  # Book table (0 or 1)
        
        # For location, rest_type, type, and city, handle as strings
        location = request.form['location']
        rest_type = request.form['rest_type']
        type_ = request.form['type']
        city = request.form['city']

        # If these are categorical variables and you need to convert them to numeric values:
        # Example of conversion for categorical variables (you need encoding logic or mapping)
        # You can create a dictionary for encoding or use one-hot encoding, if necessary.
        # Example: If location is 'BTM', you can map it to an integer.

        location_mapping = {'Koramangala 5th Block': 1, 'BTM': 2, 'Indiranagar': 3, 'KR Puram': 4, 'Kanakapura': 5, 'Magadi Road': 6}
        rest_type_mapping = {'Casual Dining': 1, 'Quick Bites': 2, 'Cafe': 3, 'Dessert Parlor': 4, 'Food Court': 5, 'Dhaba': 6}
        type_mapping = {'North Indian': 1, 'South Indian': 2, 'Chinese': 3, 'Italian': 4, 'Pasta': 5, 'Pizza': 6}
        city_mapping = {'Bangalore': 1}

        location = location_mapping.get(location, 0)  # Default to 0 if not found in mapping
        rest_type = rest_type_mapping.get(rest_type, 0)  # Default to 0 if not found
        type_ = type_mapping.get(type_, 0)  # Default to 0 if not found
        city = city_mapping.get(city, 0)  # Default to 0 if not found

        # Combine features into one array
        features = np.array([[votes, cost, online_order, book_table, location, rest_type, type_, city]])
        
        # Scale features
        final_features = scaler.transform(features)
        
        # Predict the rating
        prediction = model.predict(final_features)

        return render_template('index.html', prediction_text=f'🌟 Predicted Rating: {prediction[0]:.2f}')
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)



