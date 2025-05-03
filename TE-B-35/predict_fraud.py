import numpy as np
import joblib
import os

def load_model_and_scaler():
    # Check if model and scaler files exist
    if not os.path.exists('fraud_model.pkl') or not os.path.exists('scaler.pkl'):
        print("Model or scaler files not found. Run train_model.py first.")
        return None, None, None
    
    # Load the model and scaler
    model = joblib.load('fraud_model.pkl')
    scaler = joblib.load('scaler.pkl')
    
    # Load feature names
    with open('feature_names.txt', 'r') as f:
        feature_names = f.read().split(',')
    
    return model, scaler, feature_names

def get_user_input(feature_names):
    """Get transaction details from user input"""
    print("\n=== Credit Card Fraud Detection System ===")
    print("Please enter the transaction details:")
    
    user_input = {}
    
    # Get input for each feature
    for feature in feature_names:
        while True:
            try:
                value = float(input(f"{feature} (number): "))
                user_input[feature] = value
                break
            except ValueError:
                print("Please enter a valid number.")
    
    return user_input

def predict_fraud(user_input, model, scaler, feature_names):
    """Predict if a transaction is fraudulent"""
    # Convert user input to numpy array in the correct order
    input_array = np.array([user_input[feature] for feature in feature_names]).reshape(1, -1)
    
    # Scale the input
    scaled_input = scaler.transform(input_array)
    
    # Make prediction
    prediction = model.predict(scaled_input)[0]
    probability = model.predict_proba(scaled_input)[0][1]  # Probability of fraud
    
    return prediction, probability

def explain_prediction(user_input, feature_names, prediction, probability):
    """Provide explanation of the prediction result"""
    print("\n=== Prediction Result ===")
    
    if prediction == 1:
        print("⚠️ POTENTIAL FRAUD DETECTED ⚠️")
        print(f"Fraud probability: {probability:.2%}")
        print("\nThis transaction was flagged as potentially fraudulent.")
    else:
        print("✅ TRANSACTION APPEARS LEGITIMATE")
        print(f"Fraud probability: {probability:.2%}")
        print("\nThis transaction does not appear to be fraudulent.")
    
    # If there's high probability, highlight key factors
    if probability > 0.3:  # Threshold for explanation
        print("\nKey factors that contributed to this assessment:")
        if user_input['amount'] > 200:
            print(f"- Transaction amount (${user_input['amount']:.2f}) is higher than typical")
        if abs(user_input['v1']) > 2:
            print(f"- Unusual pattern detected in transaction characteristics (v1)")
        if abs(user_input['v3']) > 2:
            print(f"- Unusual pattern detected in transaction characteristics (v3)")

def provide_example_values():
    """Provide example values for the user to try"""
    print("\n=== Example Values ===")
    print("For a likely legitimate transaction, try:")
    print("amount: 75.5, time: 12.5, v1: 0.5, v2: 0.2, v3: 0.1, v4: -0.5, v5: 0.3")
    print("\nFor a likely fraudulent transaction, try:")
    print("amount: 350.75, time: 3.25, v1: -2.5, v2: 0.2, v3: 2.5, v4: -0.5, v5: 0.3")

def main():
    # Load model, scaler and feature names
    model, scaler, feature_names = load_model_and_scaler()
    
    if model is None:
        print("Please run train_model.py first to generate the model.")
        return
    
    # Provide example values
    provide_example_values()
    
    while True:
        # Get user input
        user_input = get_user_input(feature_names)
        
        # Make prediction
        prediction, probability = predict_fraud(user_input, model, scaler, feature_names)
        
        # Explain prediction
        explain_prediction(user_input, feature_names, prediction, probability)
        
        # Ask if user wants to try another prediction
        try_again = input("\nWould you like to try another prediction? (y/n): ").lower()
        if try_again != 'y':
            print("Thank you for using the Credit Card Fraud Detection System!")
            break

if __name__ == "__main__":
    main() 