import pandas as pd # type: ignore
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.linear_model import LogisticRegression # type: ignore
from sklearn.tree import DecisionTreeClassifier # type: ignore
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.metrics import classification_report # type: ignore
import pickle
from fastapi import FastAPI, HTTPException # type: ignore
from fastapi.middleware.cors import CORSMiddleware  # type: ignore # Import CORS middleware
from pydantic import BaseModel # type: ignore

# Load the data
data_fake = pd.read_csv(r"C:/Users/asus/Desktop/fackNewsDection/datasets/Fake.csv")
data_true = pd.read_csv(r"C:/Users/asus/Desktop/fackNewsDection/datasets/True.csv")

# Add class labels
data_fake["class"] = 0
data_true['class'] = 1

# Merge datasets
data_merge = pd.concat([data_fake, data_true], axis=0)
data = data_merge.drop(['title', 'subject', 'date'], axis=1)

# Shuffle the data
data = data.sample(frac=1).reset_index(drop=True)

# Preprocessing function
def wordopt(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

# Apply preprocessing
data['text'] = data['text'].apply(wordopt)

# Define dependent and independent variables
x = data['text']
y = data['class']

# Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

# Vectorize the text data
vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)

# Train Logistic Regression model
LR = LogisticRegression()
LR.fit(xv_train, y_train)

# Save the model and vectorizer
pickle.dump(LR, open("model.pkl", "wb"))
pickle.dump(vectorization, open("vectorizer.pkl", "wb"))

# FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for testing only)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load trained model & vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Define input model
class NewsItem(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Fake News Detection API is Running"}

@app.post("/predict/")
def predict(news: NewsItem):
    try:
        processed_text = wordopt(news.text)
        transformed_text = vectorizer.transform([processed_text])
        prediction = model.predict(transformed_text)[0]
        return {"prediction": "Fake News" if prediction == 0 else "Not Fake News"}  # Fixed typo: "prediction"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run FastAPI
if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app, host="localhost", port=8080) 
