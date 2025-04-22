# 🏦 Loan Approval Prediction System

A smart and intuitive machine learning-based web app that predicts whether a loan will be approved based on applicant details. Built with **Flask**, styled with **Bootstrap**, and powered by a trained **scikit-learn model**.

---

## 🚀 Features

- **Loan Form Input**: Simple UI to enter all relevant loan parameters.
- **ML-Powered Predictions**: Uses a trained classification model to approve or reject.
- **Confidence Score**: Displays the model's confidence percentage.
- **Dark Mode**: User-friendly dark/light mode toggle.
- **Responsive Design**: Mobile-friendly and animated UI.

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Flask (Python)
- **Model**: scikit-learn, joblib
- **Deployment**: Render

---

## 📦 Project Structure

```
Loan-Approval-Prediction-System/
├── csv/
│   ├── test.csv
│   └── train.csv
├── Flask/
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   └── index.html
│   ├── app.py
├── loan_approval_model_optimized.pkl
├── loan_approval_model.pkl
├── Untitled.ipynb
├── README.md
```

---

## 💻 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Viole07/Loan-Approval-Prediction-System.git
cd Loan-Approval-Prediction-System/Flask
```

### 2. Install Required Packages
```bash
pip install flask scikit-learn numpy joblib
```

### 3. Run the Flask App
```bash
python app.py
```

Navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📸 Screenshots

### 🟡 1. Rejection Form Filled
Loan form is filled with values likely to result in a rejection.

![Rejection Form](screenshots/rejection-form.png)

---

### ❌ 2. Rejected Prediction Output
The loan is rejected with a displayed confidence score.

![Rejected](screenshots/rejected-result.png)

---

### 🟢 3. Acceptance Form Filled
Form updated with values more likely to be approved.

![Acceptance Form](screenshots/acceptance-form.png)

---

### ✅ 4. Approved Prediction Output
The loan is approved along with a confidence percentage.

![Approved](screenshots/approved-result.png)

---

## 🔐 .gitignore Example
```gitignore
__pycache__/
venv/
*.pkl
.env
*.csv
.DS_Store
```

---

## 📜 License
MIT License — free to use, modify, and distribute.

---

Built with ❤️ by [@Viole07](https://github.com/Viole07)

