import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

def load_data(file_path=None):
    """
    Load data from a file or create sample data if file doesn't exist
    """
    if file_path and os.path.exists(file_path):
        # Load data from file
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return create_sample_data()
    else:
        # Create sample data
        return create_sample_data()

def create_sample_data():
    """
    Create sample thyroid data for demonstration
    """
    np.random.seed(42)
    
    # Sample size
    n_samples = 1000
    
    # Generate features
    age = np.random.normal(45, 15, n_samples).clip(18, 90)
    
    # TSH levels: Normal (0.4-4.0), Hypothyroidism (>4.0), Hyperthyroidism (<0.4)
    tsh_normal = np.random.uniform(0.4, 4.0, int(n_samples * 0.6))
    tsh_hypo = np.random.uniform(4.1, 15.0, int(n_samples * 0.25))
    tsh_hyper = np.random.uniform(0.01, 0.39, int(n_samples * 0.15))
    tsh = np.concatenate([tsh_normal, tsh_hypo, tsh_hyper])
    
    # T3 levels: Normal (80-200), Hypothyroidism (<80), Hyperthyroidism (>200)
    t3_normal = np.random.uniform(80, 200, int(n_samples * 0.6))
    t3_hypo = np.random.uniform(40, 79, int(n_samples * 0.25))
    t3_hyper = np.random.uniform(201, 300, int(n_samples * 0.15))
    t3 = np.concatenate([t3_normal, t3_hypo, t3_hyper])
    
    # T4 levels: Normal (5-12), Hypothyroidism (<5), Hyperthyroidism (>12)
    t4_normal = np.random.uniform(5, 12, int(n_samples * 0.6))
    t4_hypo = np.random.uniform(1, 4.9, int(n_samples * 0.25))
    t4_hyper = np.random.uniform(12.1, 20, int(n_samples * 0.15))
    t4 = np.concatenate([t4_normal, t4_hypo, t4_hyper])
    
    # Gender (1 for male, 0 for female)
    gender = np.random.randint(0, 2, n_samples)
    
    # Create labels based on hormone levels (0: normal, 1: hypothyroidism, 2: hyperthyroidism)
    labels = np.zeros(n_samples, dtype=int)
    
    # Assign hypothyroidism
    hypo_mask = (tsh > 4.0) | (t4 < 5) | (t3 < 80)
    labels[hypo_mask] = 1
    
    # Assign hyperthyroidism
    hyper_mask = (tsh < 0.4) | (t4 > 12) | (t3 > 200)
    labels[hyper_mask] = 2
    
    # Ensure some consistency in the data
    for i in range(n_samples):
        if labels[i] == 1:  # Hypothyroidism
            if np.random.random() < 0.8:  # 80% chance to have consistent values
                tsh[i] = np.random.uniform(4.1, 15.0)
                t4[i] = np.random.uniform(1, 4.9)
                t3[i] = np.random.uniform(40, 79)
        elif labels[i] == 2:  # Hyperthyroidism
            if np.random.random() < 0.8:  # 80% chance to have consistent values
                tsh[i] = np.random.uniform(0.01, 0.39)
                t4[i] = np.random.uniform(12.1, 20)
                t3[i] = np.random.uniform(201, 300)
    
    # Create DataFrame
    data = pd.DataFrame({
        'age': age[:n_samples],
        'tsh': tsh[:n_samples],
        't3': t3[:n_samples],
        't4': t4[:n_samples],
        'gender': gender[:n_samples],
        'condition': labels[:n_samples]
    })
    
    return data

def train_model(data=None):
    """
    Train a model on the provided data or sample data
    """
    if data is None:
        data = create_sample_data()
    
    # Split features and target
    X = data[['age', 'tsh', 't3', 't4', 'gender']]
    y = data['condition']
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    print(f"Model Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(report)
    
    # Save model and scaler
    os.makedirs('models', exist_ok=True)
    with open('models/thyroid_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('models/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    
    return model, scaler, accuracy

if __name__ == "__main__":
    # This will create sample data, train and save the model
    data = create_sample_data()
    
    # Save sample data for reference
    os.makedirs('data', exist_ok=True)
    data.to_csv('data/thyroid_sample_data.csv', index=False)
    
    # Train and save model
    model, scaler, accuracy = train_model(data)
    
    print(f"Sample data saved to data/thyroid_sample_data.csv")
    print(f"Model saved to models/thyroid_model.pkl with accuracy: {accuracy:.4f}")