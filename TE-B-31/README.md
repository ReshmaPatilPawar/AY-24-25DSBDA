
# 📧 Spam Mail Detection System

An intelligent spam mail classifier web application built using **React**, **Tailwind CSS**, and **Framer Motion** on the frontend, and **Flask** with a trained **Machine Learning model** on the backend. The backend is containerized using **Docker**.

---

## 🔍 Project Overview

This project allows users to input an email message and predict whether it is **Spam** or **Not Spam (Ham)**. The application uses a trained Logistic Regression model and TF-IDF vectorizer to classify messages in real-time.

---

## ⚙️ Tech Stack

### ✅ Frontend:
- React.js – For building the UI
- Tailwind CSS – For responsive styling
- Framer Motion – For smooth animations

### ✅ Backend:
- Flask – Lightweight Python web framework
- Scikit-learn – For Machine Learning
- Pickle – For saving/loading the model & vectorizer
- Docker – For containerizing the backend

---

## 📁 Project Structure

```
📦 spam-mail-detection
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   └── index.css
│   └── tailwind.config.js
├── backend/
│   ├── main.py
│   ├── spam_model.pkl
│   ├── vectorizer.pkl
│   ├── Dockerfile
│   └── requirements.txt
└── README.md
```

---

## 🧠 Machine Learning Details

- **Algorithm Used:** Logistic Regression
- **Vectorizer:** TF-IDF (Term Frequency-Inverse Document Frequency)
- **Dataset:** Labeled CSV of spam and ham emails
- **Accuracy:** Achieved high accuracy (up to 1.0 on training/test data)

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/spam-mail-detection.git
cd spam-mail-detection
```

---

### 2️⃣ Run the Flask Backend Locally (without Docker)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

This starts the backend at: `http://127.0.0.1:5000`

---

### 3️⃣ OR Pull & Run the Dockerized Backend

```bash
docker pull codercastor/spam-mail-api
docker run -p 8000:5000 codercastor/spam-mail-api
```

Now your backend runs at: `http://localhost:8000`

---

### 4️⃣ Run the React Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://localhost:5173`

---

## 📡 API Endpoint

**POST** `/predict`

**URL:** `http://localhost:5000/predict`

**Request Body:**

```json
{
  "message": "Congratulations! You've won a free cruise. Click to claim."
}
```

**Response:**

```json
{
  "prediction": "Spam"
}
```

---

## 🖼 UI Highlights

- Mobile-first responsive design with Tailwind CSS
- Animated transitions using Framer Motion
- Simple, clean, and intuitive UI

---

## 🐳 Docker Info

This project’s backend is fully containerized.

➡️ Pull the image:

```bash
docker pull codercastor/spam-mail-api
```

➡️ Run the container:

```bash
docker run -p 5000:5000 codercastor/spam-mail-api
```

---

## 👨‍💻 Author

- **Name:** Tejas Shinde 
- **Email:** tejasshinde935@gmail.com  
- **GitHub:** [codercastor](https://github.com/codercastor)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
