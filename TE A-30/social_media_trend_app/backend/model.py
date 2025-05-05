# backend/model.py
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_excel("../public/Social_Media_Trends.xlsx")

# Prepare data
X = df[['Retweets']]  # Predictor
y = df['Likes']       # Target

# Fit model
model = LinearRegression()
model.fit(X, y)

# Predict likes for a new number of retweets
example_retweets = [[10]]
predicted_likes = model.predict(example_retweets)
print(f"Predicted Likes for 10 retweets: {predicted_likes[0]}")
