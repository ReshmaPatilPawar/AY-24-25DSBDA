import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("zomato.csv")

# Keep only needed columns
df = df[['online_order', 'book_table', 'location', 'rest_type', 'cuisines', 
         'approx_cost(for two people)', 'listed_in(type)', 'votes', 'rate']]

# Drop rows with missing values in important columns
df.dropna(subset=['rate', 'approx_cost(for two people)', 'votes'], inplace=True)

# Remove unwanted 'rate' values like 'NEW' or '-'
df = df[~df['rate'].isin(['NEW', '-', 'nan'])]

# Convert 'rate' to float
df['rate'] = df['rate'].apply(lambda x: str(x).split('/')[0]).astype(float)

# Clean 'approx_cost(for two people)' column (remove commas and convert to int)
df['approx_cost(for two people)'] = df['approx_cost(for two people)'].apply(lambda x: str(x).replace(',', '')).astype(float)

# Encode categorical columns
le = LabelEncoder()
for col in ['online_order', 'book_table', 'location', 'rest_type', 'cuisines', 'listed_in(type)']:
    df[col] = le.fit_transform(df[col].astype(str))

# Prepare features and target
X = df[['online_order', 'book_table', 'location', 'rest_type', 'cuisines', 
        'approx_cost(for two people)', 'listed_in(type)', 'votes']]
y = df['rate']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
