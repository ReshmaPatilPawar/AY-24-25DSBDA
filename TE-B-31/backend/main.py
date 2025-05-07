from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data['message']
    
    input_features = vectorizer.transform([message])
    prediction = model.predict(input_features)[0]
    
    result = "Ham" if prediction == 1 else "Spam"
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
