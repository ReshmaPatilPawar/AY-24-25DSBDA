# ThyroPredict - Thyroid Prediction Website

A Python Flask application that uses machine learning to predict thyroid conditions based on health data.

## Project Overview

ThyroPredict is a web application that allows users to input thyroid-related health metrics and receive predictions about their thyroid health. The application uses a machine learning model trained on thyroid health data to make these predictions.

## Features

- User-friendly interface for entering thyroid-related health data
- Machine learning model for thyroid condition prediction
- Educational information about thyroid disorders
- Results visualization with clear explanations
- Secure data handling and privacy protection
- Responsive design working across all devices
- Downloadable report generation

## Technologies Used

- Backend: Python Flask
- Data Processing: Pandas, NumPy
- Machine Learning: scikit-learn
- Frontend: HTML, CSS, JavaScript
- Styling: Custom CSS with responsive design
- Visualization: Vanilla JavaScript

## Setup and Installation

1. Clone the repository
```bash
git clone <repository-url>
cd thyropredict
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

5. Access the application at `http://localhost:5000`

## Project Structure

```
thyropredict/
├── app.py                 # Main Flask application
├── data_handler.py        # Data processing and model training
├── requirements.txt       # Python dependencies
├── models/                # Directory for saved ML models
├── data/                  # Directory for data files
├── static/                # Static assets
│   ├── css/               # CSS stylesheets
│   │   └── main.css       # Main stylesheet
│   ├── js/                # JavaScript files
│   │   └── main.js        # Main JavaScript file
│   └── img/               # Images
└── templates/             # HTML templates
    ├── index.html         # Homepage
    ├── predict.html       # Prediction form
    ├── result.html        # Prediction results
    ├── about.html         # About thyroid health
    └── error.html         # Error page
```

## How to Use

1. Navigate to the home page and click on "Try Prediction Tool"
2. Fill in the required health data (age, gender, TSH, T3, T4)
3. Submit the form to get a prediction
4. View your results and the interpretation of what they mean
5. Optionally print or save your results

## Model Information

The prediction model is a Random Forest Classifier trained on thyroid health data. It considers the following features:

- Age
- TSH (Thyroid Stimulating Hormone) level
- T3 (Triiodothyronine) level
- T4 (Thyroxine) level
- Gender

The model can predict three possible outcomes:
- Normal Thyroid Function
- Hypothyroidism (Underactive Thyroid)
- Hyperthyroidism (Overactive Thyroid)

## Developer Information

- To retrain the model with new data, run `python data_handler.py`
- The prediction logic is contained in the `/predict` route in `app.py`
- Frontend styling can be modified in `static/css/main.css`

## Disclaimer

This tool is for educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with a healthcare provider for medical concerns.