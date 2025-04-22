import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model  

import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.preprocessing import MinMaxScaler

# Page configuration
st.set_page_config(page_title="Stock Price Predictor")

# Title
st.title("📈 Stock Price Predictor App")

# User Input for Stock Symbol
stock = st.text_input("Enter Stock Symbol:", "GOOG")

# Load Data
from datetime import datetime
end = datetime.now()
start = datetime(end.year - 20, end.month, end.day)
google_data = yf.download(stock, start, end)
google_data.columns = google_data.columns.droplevel(1) if isinstance(google_data.columns, pd.MultiIndex) else google_data.columns

# Load Model
model = load_model("Latest_stock_price_model.keras")

# Display Stock Data
st.subheader("📊 Stock Data")
st.dataframe(google_data)

# Splitting Data
splitting_len = int(len(google_data) * 0.7)
x_test = pd.DataFrame(google_data['Close'][splitting_len:], columns=['Close'])

# Normalize Data
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(x_test)

x_data, y_data = [], []
for i in range(100, len(scaled_data)):
    x_data.append(scaled_data[i-100:i])
    y_data.append(scaled_data[i])

x_data, y_data = np.array(x_data), np.array(y_data)

# Predict
predictions = model.predict(x_data)

# Inverse Transform
inv_pre = scaler.inverse_transform(predictions)
inv_y_test = scaler.inverse_transform(y_data)

# Create DataFrame for Comparison
ploting_data = pd.DataFrame(
    {'Original Data': inv_y_test.reshape(-1), 'Predicted Data': inv_pre.reshape(-1)},
    index=google_data.index[splitting_len+100:]
)

st.subheader("📉 Predictions vs Actual Data")
st.dataframe(ploting_data)

# Interactive Graphs
def create_interactive_chart(df, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index, y=df['Close'],
        mode='lines', name='Close Price',
        line=dict(color='orange', width=2),
        hoverinfo='x+y'
    ))
    fig.update_layout(
        title=title, xaxis_title='Date', yaxis_title='Price',
        paper_bgcolor='white', plot_bgcolor='white'
    )
    return fig

st.plotly_chart(create_interactive_chart(google_data, "📊 Stock Close Price"))

# Interactive Prediction Graph
fig = make_subplots()
fig.add_trace(go.Scatter(
    x=ploting_data.index, y=ploting_data['Original Data'],
    mode='lines', name='Actual Price',
    line=dict(color='green', width=2),
    hoverinfo='x+y'
))
fig.add_trace(go.Scatter(
    x=ploting_data.index, y=ploting_data['Predicted Data'],
    mode='lines', name='Predicted Price',
    line=dict(color='red', width=2),
    hoverinfo='x+y'
))
fig.update_layout(
    title='Predicted vs Actual Prices', xaxis_title='Date', yaxis_title='Price',
    paper_bgcolor='white', plot_bgcolor='white'
)
st.plotly_chart(fig)
