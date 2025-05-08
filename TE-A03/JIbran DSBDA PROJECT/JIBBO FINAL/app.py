import os
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

try:
    with open(model_path, 'rb') as f:
        data = pickle.load(f)
        model = data['model']
        encoders = data['encoders']
except Exception as e:
    raise RuntimeError(f"Failed to load model from {model_path}: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form = request.form
        input_data = []
        for field in ['team1', 'team2', 'toss_winner', 'toss_decision', 'venue']:
            value = form.get(field)
            if value is None:
                return render_template('index.html', prediction="Missing input: " + field)
            encoded = encoders[field].transform([value])[0]
            input_data.append(encoded)

        pred = model.predict([input_data])[0]
        prediction = encoders['winner'].inverse_transform([pred])[0]
        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
