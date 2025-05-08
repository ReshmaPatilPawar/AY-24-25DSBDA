import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Generate synthetic data for credit card fraud detection
def generate_synthetic_data(n_samples=10000):
    np.random.seed(42)
    
    # Create features
    amount = np.random.exponential(scale=100, size=n_samples)
    time = np.random.uniform(0, 24, size=n_samples)
    v1 = np.random.normal(0, 1, size=n_samples)
    v2 = np.random.normal(0, 1, size=n_samples)
    v3 = np.random.normal(0, 1, size=n_samples)
    v4 = np.random.normal(0, 1, size=n_samples)
    v5 = np.random.normal(0, 1, size=n_samples)
    
    # Create the fraud labels (about 0.5% fraud rate)
    fraud = np.zeros(n_samples)
    fraud_indices = np.random.choice(np.arange(n_samples), size=int(0.005 * n_samples), replace=False)
    fraud[fraud_indices] = 1
    
    # Adjust feature distributions for fraud cases
    amount[fraud == 1] = amount[fraud == 1] * 2.5
    v1[fraud == 1] = v1[fraud == 1] - 2
    v3[fraud == 1] = v3[fraud == 1] + 1.5
    
    # Create DataFrame
    data = pd.DataFrame({
        'amount': amount,
        'time': time,
        'v1': v1,
        'v2': v2,
        'v3': v3,
        'v4': v4,
        'v5': v5,
        'fraud': fraud
    })
    
    return data

# Main function to train and save the model
def train_fraud_model():
    print("Generating synthetic credit card transaction data...")
    data = generate_synthetic_data()
    
    # Split features and target
    X = data.drop('fraud', axis=1)
    y = data['fraud']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train the model
    print("Training Random Forest classifier...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train_scaled, y_train)
    
    # Evaluate the model
    y_pred = clf.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the model and scaler
    print("Saving model and scaler...")
    joblib.dump(clf, 'fraud_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    
    # Save feature names
    with open('feature_names.txt', 'w') as f:
        f.write(','.join(X.columns))
    
    print("Model training complete!")

if __name__ == "__main__":
    train_fraud_model() 