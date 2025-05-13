from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('heart_model_simple.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form
        input_data = np.array([
            float(form['age']),
            float(form['trestbps']),
            float(form['chol']),
            float(form['thalch']),
            float(form['oldpeak']),
        ]).reshape(1, -1)
        prediction = model.predict(input_data)[0]
        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
        return render_template('form.html', result=result)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
