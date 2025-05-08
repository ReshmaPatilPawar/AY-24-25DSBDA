import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler

@st.cache_data
def load_data():
    """
    Load and preprocess the nutrition data
    """
    try:
        # Try to load the data from the data directory
        df = pd.read_csv('data/nutrition_value_dataset.csv', sep=',', encoding='UTF-8')
    except FileNotFoundError:
        # If file not found, use the sample data
        df = create_sample_data()
    
    # Clean column names
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.rstrip()
    
    # Fill missing values with 0 for numeric columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)
    
    return df

def create_sample_data():
    """
    Create a sample DataFrame with the same structure as the expected dataset
    This is used as a fallback if the file is not found
    """
    # Create sample data with expected columns
    data = {
        'company': ['Pizza Hut', 'McDonald\'s', 'KFC', 'Burger King', 'Subway'],
        'category': ['All Meals', 'Burger', 'Fried Chicken', 'Burger', 'Sandwiches'],
        'product': ['Cheese Pizza', 'Big Mac', 'Original Recipe', 'Whopper', 'Tuna Sub'],
        'per_serve_size': ['150g', '200g', '150g', '250g', '200g'],
        'energy_(kcal)': [300, 550, 400, 650, 450],
        'carbohydrates_(g)': [40, 45, 30, 50, 40],
        'protein_(g)': [15, 25, 20, 30, 25],
        'fiber_(g)': [2, 3, 1, 2, 5],
        'sugar_(g)': [5, 10, 0, 10, 5],
        'total_fat_(g)': [10, 30, 25, 35, 20],
        'saturated_fat_(g)': [5, 10, 10, 15, 8],
        'trans_fat_(g)': [0, 1, 0.5, 1.5, 0],
        'cholesterol_(mg)': [20, 80, 90, 85, 30],
        'sodium_(mg)': [500, 1000, 900, 1200, 800]
    }
    
    return pd.DataFrame(data)

def get_nutrition_columns(df):
    """
    Get all nutrition-related columns
    """
    # Exclude non-numeric and identifying columns
    exclude_cols = ['company', 'category', 'product', 'per_serve_size']
    return [col for col in df.columns if col not in exclude_cols]

def format_column_name(col_name):
    """
    Format column name for display
    """
    # Remove underscores and convert to title case
    name = col_name.replace('_', ' ').title()
    
    # Remove parentheses and their contents, but keep the unit
    if '(' in name:
        unit = name[name.find('('):name.find(')')+1]
        name = name.replace(unit, '')
        name = name.strip() + ' ' + unit
    
    return name

def create_comparison_chart(df, products, metric):
    """
    Create a comparison chart for selected products and a specific metric
    """
    # Filter data for the selected products
    comparison_df = df[df['product'].isin(products)].copy()
    
    # Sort by the selected metric
    comparison_df = comparison_df.sort_values(by=metric)
    
    # Create a horizontal bar chart
    fig = px.bar(
        comparison_df,
        y='product',
        x=metric,
        color='company',
        title=f'Comparison of {format_column_name(metric)} across Products',
        labels={
            'product': 'Product',
            metric: format_column_name(metric)
        },
        orientation='h'
    )
    
    return fig


@st.cache_resource
def build_prediction_model(df, target_col='energy_(kcal)', test_size=0.25):
    """
    Build a prediction model to estimate nutritional values
    
    Parameters:
    -----------
    df : pandas DataFrame
        The nutrition data
    target_col : str
        The target column to predict
    test_size : float
        The proportion of the dataset to include in the test split
        
    Returns:
    --------
    dict
        Dictionary containing the trained model, scaler, feature columns,
        and evaluation metrics
    """
    # Get nutrition columns for features
    nutrition_cols = get_nutrition_columns(df)
    
    # Remove the target column from features
    feature_cols = [col for col in nutrition_cols if col != target_col]
    
    # Prepare features and target
    X = df[feature_cols].values
    y = df[target_col].values
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train a Linear Regression model
    lr_model = LinearRegression()
    lr_model.fit(X_train_scaled, y_train)
    
    # Make predictions
    lr_y_pred = lr_model.predict(X_test_scaled)
    
    # Evaluate the linear model
    lr_mse = mean_squared_error(y_test, lr_y_pred)
    lr_rmse = np.sqrt(lr_mse)
    lr_mae = mean_absolute_error(y_test, lr_y_pred)
    lr_r2 = r2_score(y_test, lr_y_pred)
    
    # Train a Random Forest model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train_scaled, y_train)
    
    # Make predictions
    rf_y_pred = rf_model.predict(X_test_scaled)
    
    # Evaluate the random forest model
    rf_mse = mean_squared_error(y_test, rf_y_pred)
    rf_rmse = np.sqrt(rf_mse)
    rf_mae = mean_absolute_error(y_test, rf_y_pred)
    rf_r2 = r2_score(y_test, rf_y_pred)
    
    # Select the best model based on R2 score
    if rf_r2 > lr_r2:
        best_model = rf_model
        model_name = "Random Forest"
        metrics = {
            'mse': rf_mse,
            'rmse': rf_rmse,
            'mae': rf_mae,
            'r2': rf_r2
        }
    else:
        best_model = lr_model
        model_name = "Linear Regression"
        metrics = {
            'mse': lr_mse,
            'rmse': lr_rmse,
            'mae': lr_mae,
            'r2': lr_r2
        }
    
    # Return the model, scaler, feature columns, and metrics
    return {
        'model': best_model,
        'scaler': scaler,
        'feature_cols': feature_cols,
        'metrics': metrics,
        'model_name': model_name,
        'target_col': target_col,
        'feature_importance': None if model_name == "Linear Regression" else {
            feature_cols[i]: importance 
            for i, importance in enumerate(best_model.feature_importances_) if hasattr(best_model, 'feature_importances_')
        }
    }
