# Saheli - PCOS PREDICTION

SARGAM SHRIKANT PURAM
T.E. B - 16
DSBDA

Frontend Link - https://saheli-liard.vercel.app/
Backend Link - https://pcos-prediction-backend.onrender.com/

PCOS Prediction and Care platform

![image](https://github.com/user-attachments/assets/d477913b-7053-48f1-9ca7-976d7537a6af)


## What is PCOS?

Polycystic Ovary Syndrome (PCOS) is one of the most common hormonal disorders among women of reproductive age. It affects millions of women worldwide and can lead to irregular periods, difficulty getting pregnant, and other health issues. Unfortunately, many women remain undiagnosed or struggle to manage the condition effectively, making it essential to spread awareness and offer better solutions.

## How PCOS Affects Women

PCOS can manifest in several ways, and its symptoms can vary from person to person. Common symptoms include:

- **Irregular periods** or no periods at all
- **Excess androgen (male hormone)** levels, leading to symptoms like acne, facial hair growth, and male-pattern baldness
- **Weight gain** or difficulty losing weight
- **Ovulation problems**, making it harder to get pregnant
- **Skin problems**, such as oily skin or acanthosis nigricans (dark, velvety patches of skin on the back of the neck, armpits, or groin)
- **Sleep apnea**
- **Mood swings** and depression

![image](https://github.com/user-attachments/assets/197a298c-78cd-4b1b-9631-f56b15dff50f)


## What We Offer

At **Saheli**, we are committed to empowering women with the knowledge and support they need to manage PCOS. Our platform offers:

- **Personalized Health Insights**: Based on your symptoms and medical history, we provide tailored health recommendations.
- **Lifestyle Guidance**: Receive expert advice on how to make lifestyle changes that effectively manage PCOS.
- **Emotional Support**: Our AI assistant, Saheli, is designed to offer emotional support and a compassionate ear.
- 
- ![Screenshot 2025-01-24 144855](https://github.com/user-attachments/assets/598decc3-55b3-41ef-8416-3c324f8c48d0)

## Prediction & Chatbot Feature

Our platform leverages **advanced Machine Learning** models to predict PCOS and guide users in managing the condition. We utilize IBM's powerful **Watson** technology to provide personalized care plans and predictions based on historical data.

### Features:
- **PCOS Prediction**: Saheli uses predictive analytics to assess your symptoms and predict the likelihood of PCOS, offering a clear pathway for care.
- **Chatbot Support**: Powered by **IBM Watson AI**, our chatbot Saheli provides emotional support, answers questions, and guides users through lifestyle adjustments, all with a friendly tone and personalized care.

![Screenshot 2025-01-24 153047](https://github.com/user-attachments/assets/6d529cce-c803-4090-a2c7-3816145f96f8)

## Our Mission

At Saheli, we live by our mission:  
**"A healthy woman is a powerful woman."**

We believe that by providing the right tools, support, and education, we can help women with PCOS lead healthier, more fulfilling lives. Every woman deserves to be the best version of herself, and we are here to help make that happen.

## Why IBM Watson?

Saheli’s foundation is built on IBM's **Watson AI** technology, which plays a pivotal role in our mission to provide personalized care. With Watson, we are able to deliver cutting-edge solutions for health predictions, chatbot assistance, and customized guidance, ensuring that women not only receive the best information but also the most compassionate support. 

We are proud to be part of the **IBM Hackathon** and are excited about how Watson's capabilities are transforming our approach to health management.

## Frontend Technology

The frontend of Saheli is built using React, a popular JavaScript library for building user interfaces. With React, we have been able to create a dynamic and responsive platform that provides a smooth user experience.Additionally, React's ecosystem, including tools like React Router for navigation, helps create a seamless and intuitive user flow.


## Backend Technology

Our backend is powered by **FastAPI**, offering high performance, rapid response times, and a secure foundation for all our features. FastAPI ensures that our users can access the platform seamlessly, whether they're seeking health insights or chatting with Saheli for support.

## Running Frontend Locally

1. Clone the repository:

```bash
git clone https://github.com/<your-github-username>/Saheli.git
```
2. Navigate to frontend
   
```bash
cd frontend
```

4. Install dependencies:
```bash
npm install
```

5. Start the development server
```bash
npm run dev
```

## Running Backend Locally

1. Clone the repository:

```bash
git clone https://github.com/<your-github-username>/Saheli.git
```
2. Navigate to backend
   
```bash
cd backend/my-flask-app
```

3. Create a virtual environment named 'venv'
```bash
python -m venv venv
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Start the uvicorn server
```bash
uvicorn app:app --reload
```

6. To Deactivate the virtual environment:
```bash
deactivate
```
To generate requirements.txt:
```bash
pip freeze > requirements.txt
```
## Sample cURL request - For Healthy Women
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 30.0,
  "marriageStatus": 0.0,
  "weight": 70.0,
  "bmi": 23.5,
  "follicleNoR": 18.0,
  "follicleNoL": 18.0,
  "amh": 5.0,
  "regularCycle": 1.0,
  "cycleLength": 30.0,
  "skinDarkening": 1.0,
  "hairGrowth": 1.0,
  "weightGain": 1.0,
  "fastFood": 1.0,
  "pimples": 1.0
}'
```
Sample Response
```bash
{"atRisk":false}
```
## Sample cURL request - For PCOS Risk Prone Women
```bash
curl -X 'POST' \
'http://127.0.0.1:8000/' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 36.0,
  "marriageStatus": 1.0,
  "weight": 72.0,
  "bmi": 25.0,
  "follicleNoR": 14.0,
  "follicleNoL": 15.0,
  "amh": 3.0,
  "regularCycle": 1.0,
  "cycleLength": 30.0,
  "skinDarkening": 0.0,
  "hairGrowth": 0.0,
  "weightGain": 3.0,
  "fastFood": 4.0,
  "pimples": 2.0
}'
```
Sample Response
```bash
{"atRisk":true}
```






