import streamlit as st
import pandas as pd
import pickle


st.title("Uber fare prediction")




passenger_count = st.number_input("Enter the number of passengers", min_value=1, max_value=6, step=1)
distance_travelled = st.number_input("Enter the distance travelled in kms", min_value=0.1, max_value=100.0, step=0.1)
month = st.number_input("Enter the month", min_value=1, max_value=12, step=1)
year = st.number_input("Enter the year", min_value=2009, max_value=2015, step=1)
day_of_the_week = st.number_input("Enter the day of the week", min_value=0, max_value=6, step=1)
pickup_hour = st.number_input("Enter the pickup hour", min_value=0, max_value=23, step=1)


# # load the model
model = pickle.load(open("models/decision_tree_model.pkl", "rb"))

predict_button = st.button("Predict")

if predict_button:

    # # predict
    prediction = model.predict([[passenger_count, distance_travelled, month, year, day_of_the_week, pickup_hour]])
    print(prediction)

    # # display
    import numpy as np
    st.write("The predicted fare amount is", np.round(prediction[0], 2))
    # display the prediction with two decimals

    # refresh the page