from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = {
        "GRE Score": float(request.form["gre"]),
        "TOEFL Score": float(request.form["toefl"]),
        "University Rating": float(request.form["rating"]),
        "SOP": float(request.form["sop"]),
        "LOR": float(request.form["lor"]),
        "CGPA": float(request.form["cgpa"]),
        "Research": int(request.form["research"])
    }

    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    result = f"Predicted Chance of Admission: {prediction:.2f}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)