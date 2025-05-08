import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load data
data = pd.read_csv('../dataset/sales_data.csv')

# Feature engineering
data['Date'] = pd.to_datetime(data['Date'])
data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

features = ['Store_ID', 'Product_ID', 'Promotion', 'Holiday', 'Day', 'Month', 'Year']
X = data[features]
y = data['Sales']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))
print("Model trained and saved successfully!")
