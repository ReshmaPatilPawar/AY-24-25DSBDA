# Customer Churn Prediction - Flask Web Application

This project is a web application built using Flask to predict customer churn using a machine learning model. The app allows users to input customer data, and based on the input, it predicts whether the customer will churn or not. The app uses machine learning models and data preprocessing techniques to provide predictions.

## Features

- **Churn Prediction**: The app predicts whether a customer will churn based on the input features.
- **User-friendly interface**: Users can input data for features like tenure, monthly charges, and more.
- **Visualization**: The output includes a pie chart that visually represents the churn/no-churn prediction.
- **Flask Web App**: Built using Flask, a lightweight web framework for Python.
- **Ngrok Integration**: The app is exposed to the internet using Flask-Ngrok for easy testing and access.

## Prerequisites

Before running the app locally or on a cloud service, ensure you have the following installed:

- Python 3.6 or higher
- pip (Python package manager)

## Setup

1. **Clone this repository**:

    ```bash
    git clone https://github.com/yourusername/churn-prediction-flask.git
    cd churn-prediction-flask
    ```

2. **Create and activate a virtual environment** (Optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Download the necessary model artifacts**:
    Ensure you have the following files in the project directory:
    - `churn_model.pkl`: The trained machine learning model.
    - `scaler.pkl`: The scaler used for feature scaling.
    - `feature_columns.pkl`: The list of feature columns used for the model.
    - `label_encoders.pkl`: The label encoders used for encoding categorical features.
    - `optimal_threshold.pkl`: The optimal threshold used for classification.

5. **Run the Flask app locally**:

    ```bash
    python app.py
    ```

6. **Access the app**:
    If running locally, you can access the app by going to `http://localhost:5000` in your web browser.

    If using Ngrok (with Flask-Ngrok), you will get a public URL to access the app.

## Project Structure


## How It Works

1. The user inputs customer data through the form in the web app (tenure, monthly charges, total charges, etc.).
2. The data is processed and passed into the machine learning model (`churn_model.pkl`) for prediction.
3. The app returns a prediction indicating whether the customer will churn or not (using emoji 🚩 for churn, ✅ for no churn).
4. A pie chart visualization is displayed, showing the proportion of churn/no-churn customers.

## Deployment

For deployment on platforms like Render, ensure that:

- All necessary model files are uploaded.
- The `requirements.txt` file is included.
- The app is configured to run on the correct port (usually 80 for production).

## Contributing

If you'd like to contribute to this project, feel free to fork it, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
