from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and column structure
model = joblib.load('models/model.pkl')
model_columns = joblib.load('models/columns.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data
    
    data = {
        'Age': int(request.form['Age']),
        'Gender': request.form['Gender'],
        'Ethnicity': request.form['Ethnicity'],
        'ParentalEducation': request.form['ParentalEducation'],
        'StudyTimeWeekly': int(request.form['StudyTimeWeekly']),
        'Absences': int(request.form['Absences']),
        'Tutoring': request.form['Tutoring'],
        'ParentalSupport': request.form['ParentalSupport'],
        'Extracurricular': request.form['Extracurricular'],
        'Sports': request.form['Sports'],
        'Music': request.form['Music'],
        'Volunteering': request.form['Volunteering']
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([data])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # Predict GPA and scale
    raw_gpa = model.predict(input_df)[0]
    gpa_10 = min(raw_gpa * 2.5, 10.0)

    return render_template('result.html', gpa=round(gpa_10, 2))

if __name__ == '__main__':
    app.run(debug=True)
