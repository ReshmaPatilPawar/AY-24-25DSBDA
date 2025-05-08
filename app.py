import streamlit as st 
import pandas as pd
import numpy as np
import joblib as jb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import streamlit_option_menu as som 

# Sidebar
with st.sidebar:
    menu_option = ['Prediction', 'Train Model']
    selected_option = som.option_menu(
        'Disease Prediction System Based on Symptoms', 
        options=menu_option, 
        icons=['hospital', 'database-fill-add', 'train-front'], 
        menu_icon='bandaid'
    )

# Load model and label encoder
model_RFC = jb.load("C:/Users/RUCHITA/disease prediction dsbda/model_RFC.pkl")
label_encoder = jb.load("C:/Users/RUCHITA/disease prediction dsbda/label_encoder.pkl")

# Prediction page
if selected_option == 'Prediction':
    st.header('Disease Prediction System based on Symptoms')
    
    # Load symptom list from severity file
    severity = pd.read_csv('C:/Users/RUCHITA/disease prediction dsbda/Diseases-Prediction-based-on-Symptoms/Dataset/Symptom-severity.csv')
    severity['Symptom'] = severity['Symptom'].str.lower().str.strip().str.replace('_',' ')
    symptom_list = severity['Symptom'].tolist()

    # Multiselect dropdown
    selected_symptoms = st.multiselect(
        "Select your symptoms",
        symptom_list,
        max_selections=17,
        placeholder="Choose up to 17 symptoms..."
    )

    def prediction(symptoms):
        symptoms = [s.lower().strip().replace('_', ' ') if s else '0' for s in symptoms]
        severity_dict = dict(zip(severity['Symptom'], severity['weight']))
        encoded = [severity_dict.get(s, 0) for s in symptoms]

        # Pad with zeros if fewer than 17 symptoms
        while len(encoded) < 17:
            encoded.append(0)
        encoded = encoded[:17]  # Limit to 17 symptoms max

        pred = model_RFC.predict([encoded])
        return label_encoder.inverse_transform(pred)[0]

    if st.button('Make Prediction'):
        if not selected_symptoms:
            st.warning("Please select at least one symptom.")
        else:
            result = prediction(selected_symptoms)
            st.success(f'Predicted Disease: {result}')

# Train model   
elif selected_option == 'Train Model':
    st.title('Model Training Page')
    st.header("Train the model")
    st.write("Click on the button to start training the model")

    def training_model():
        dataset = pd.read_csv('C:/Users/RUCHITA/disease prediction dsbda/Diseases-Prediction-based-on-Symptoms/Dataset/dataset.csv')
        for col in dataset.columns:
            dataset[col] = dataset[col].str.replace('_',' ')
        dataset = dataset.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        dataset.fillna(0, inplace=True)

        severity = pd.read_csv('C:/Users/RUCHITA/disease prediction dsbda/Diseases-Prediction-based-on-Symptoms/Dataset/Symptom-severity.csv')
        severity['Symptom'] = severity['Symptom'].str.replace('_',' ').str.strip()
        severity_dict = dict(zip(severity['Symptom'], severity['weight']))

        for col in dataset.columns[1:]:
            dataset[col] = dataset[col].apply(lambda x: severity_dict.get(x.lower(), 0) if isinstance(x, str) else 0)

        label_encoder = LabelEncoder()
        dataset['Disease'] = label_encoder.fit_transform(dataset['Disease'])

        X = dataset.drop(columns=['Disease'])
        y = dataset['Disease']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        jb.dump(model, 'model_RFC.pkl')
        jb.dump(label_encoder, 'label_encoder.pkl')

        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        return acc

    if st.button("Start Training"):
        with st.spinner("Training model..."):
            accuracy = training_model()
        st.success("✅ Model trained and saved!")
        st.success(f"Model Accuracy: {accuracy * 100:.2f}%")
