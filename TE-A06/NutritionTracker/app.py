import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data, get_nutrition_columns, create_comparison_chart, format_column_name, build_prediction_model

# Set page configuration
st.set_page_config(
    page_title="Fast Food Nutrition Dashboard",
    page_icon="🍔",
    layout="wide"
)

# Load data
df = load_data()

# Add title and description
st.title("Fast Food Nutrition Dashboard")
st.markdown("""
This dashboard allows you to explore nutrition information from various fast food restaurants. 
You can filter by company and category, compare products, and visualize nutritional components.
""")

# Sidebar filters
st.sidebar.header("Filters")

# Company filter
companies = sorted(df['company'].unique())
selected_companies = st.sidebar.multiselect(
    "Select Companies",
    options=companies,
    default=companies[:3]  # Default to first 3 companies
)

# Filter by companies
if selected_companies:
    filtered_df = df[df['company'].isin(selected_companies)]
else:
    filtered_df = df

# Category filter
categories = sorted(filtered_df['category'].unique())
selected_categories = st.sidebar.multiselect(
    "Select Categories",
    options=categories,
    default=categories[:3] if len(categories) > 3 else categories  # Default to first 3 categories
)

# Apply category filter
if selected_categories:
    filtered_df = filtered_df[filtered_df['category'].isin(selected_categories)]

# Display number of products after filtering
st.sidebar.markdown(f"**Showing {len(filtered_df)} products**")

# Main content area
if filtered_df.empty:
    st.warning("No data available with the selected filters. Please adjust your selection.")
else:
    # Overview section
    st.header("Overview")
    
    col1, col2 = st.columns(2)
    
    # Distribution of products by company
    with col1:
        fig_company = px.pie(
            filtered_df, 
            names='company', 
            title='Products by Company',
            hole=0.3
        )
        st.plotly_chart(fig_company, use_container_width=True)
    
    # Distribution of products by category
    with col2:
        company_category_counts = filtered_df.groupby(['company', 'category']).size().reset_index(name='count')
        fig_category = px.bar(
            company_category_counts, 
            x='company', 
            y='count', 
            color='category',
            title='Products by Category and Company',
            labels={'count': 'Number of Products', 'company': 'Company', 'category': 'Category'}
        )
        st.plotly_chart(fig_category, use_container_width=True)
    
    # Nutritional comparison section
    st.header("Nutritional Comparison")
    
    # Tabs for different visualization types
    tabs = st.tabs(["Product Selector", "Nutrition Distribution", "Correlation Analysis", "Nutrition Predictor"])
    tab1, tab2, tab3, tab4 = tabs
    
    with tab1:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Select specific products to compare
            select_products = st.multiselect(
                "Select products to compare (max 5)",
                options=filtered_df['product'].unique(),
                default=filtered_df['product'].unique()[:3] if len(filtered_df['product'].unique()) > 3 else filtered_df['product'].unique()[:2],
                max_selections=5
            )
            
            if select_products:
                comparison_df = filtered_df[filtered_df['product'].isin(select_products)]
                
                # Select nutrition metric to compare
                nutrition_cols = get_nutrition_columns(df)
                selected_metric = st.selectbox(
                    "Select nutrition metric to compare",
                    options=nutrition_cols,
                    index=0
                )
                
                # Create comparison chart
                fig = create_comparison_chart(comparison_df, select_products, selected_metric)
                st.plotly_chart(fig, use_container_width=True)
                
                # Display the data for selected products
                st.subheader("Data for Selected Products")
                display_cols = ['company', 'category', 'product'] + nutrition_cols
                st.dataframe(comparison_df[display_cols], use_container_width=True)
        
        with col2:
            if select_products:
                # Radar chart for comparing multiple nutritional values
                st.subheader("Nutritional Profile Comparison")
                
                radar_metrics = st.multiselect(
                    "Select metrics for radar chart",
                    options=nutrition_cols,
                    default=nutrition_cols[:5]
                )
                
                if radar_metrics:
                    # Normalize the data for radar chart
                    radar_df = comparison_df.copy()
                    for metric in radar_metrics:
                        max_val = filtered_df[metric].max()
                        radar_df[f"{metric}_norm"] = radar_df[metric] / max_val
                    
                    # Create radar chart
                    radar_data = []
                    for product in select_products:
                        product_data = radar_df[radar_df['product'] == product]
                        values = [product_data[f"{metric}_norm"].values[0] for metric in radar_metrics]
                        # Close the polygon by repeating the first value
                        values.append(values[0])
                        radar_data.append({
                            'product': product,
                            'metrics': radar_metrics + [radar_metrics[0]],
                            'values': values
                        })
                    
                    # Create the radar chart using plotly
                    fig = go.Figure()
                    
                    for data in radar_data:
                        fig.add_trace(go.Scatterpolar(
                            r=data['values'],
                            theta=data['metrics'],
                            fill='toself',
                            name=data['product']
                        ))
                    
                    fig.update_layout(
                        polar=dict(
                            radialaxis=dict(
                                visible=True,
                                range=[0, 1]
                            )
                        ),
                        showlegend=True
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        # Display distribution of nutritional values
        st.subheader("Nutrition Distribution by Company")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Select nutrition metric for distribution
            dist_metric = st.selectbox(
                "Select nutrition metric for distribution",
                options=nutrition_cols,
                index=0,
                key="dist_metric"
            )
            
            # Distribution plot
            fig = px.box(
                filtered_df, 
                x='company', 
                y=dist_metric,
                color='company',
                title=f'Distribution of {format_column_name(dist_metric)} by Company',
                labels={dist_metric: format_column_name(dist_metric), 'company': 'Company'}
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Top 10 products by selected metric
            metric_for_top = st.selectbox(
                "Select metric for top products",
                options=nutrition_cols,
                index=0,
                key="top_metric"
            )
            
            sort_order = st.radio(
                "Sort order",
                options=["Highest", "Lowest"],
                horizontal=True
            )
            
            # Sort and get top 10
            if sort_order == "Highest":
                top_products = filtered_df.sort_values(by=metric_for_top, ascending=False).head(10)
                title = f'Top 10 Products with Highest {format_column_name(metric_for_top)}'
            else:
                top_products = filtered_df.sort_values(by=metric_for_top, ascending=True).head(10)
                title = f'Top 10 Products with Lowest {format_column_name(metric_for_top)}'
            
            fig = px.bar(
                top_products,
                x=metric_for_top,
                y='product',
                color='company',
                orientation='h',
                title=title,
                labels={metric_for_top: format_column_name(metric_for_top), 'product': 'Product'}
            )
            fig.update_layout(yaxis={'categoryorder': 'total ascending'})
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        # Correlation analysis
        st.subheader("Correlation Between Nutritional Values")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Correlation matrix
            correlation_df = filtered_df[nutrition_cols].corr()
            
            fig = px.imshow(
                correlation_df,
                x=correlation_df.columns,
                y=correlation_df.columns,
                color_continuous_scale='RdBu_r',
                title='Correlation Between Nutritional Values',
                labels={'color': 'Correlation'}
            )
            fig.update_layout(
                xaxis={'tickangle': 45},
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Scatter plot for two selected metrics
            x_metric = st.selectbox(
                "X-axis metric",
                options=nutrition_cols,
                index=0,
                key="x_metric"
            )
            
            y_metric = st.selectbox(
                "Y-axis metric",
                options=nutrition_cols,
                index=1 if len(nutrition_cols) > 1 else 0,
                key="y_metric"
            )
            
            fig = px.scatter(
                filtered_df,
                x=x_metric,
                y=y_metric,
                color='company',
                hover_name='product',
                title=f'Relationship Between {format_column_name(x_metric)} and {format_column_name(y_metric)}',
                labels={
                    x_metric: format_column_name(x_metric),
                    y_metric: format_column_name(y_metric)
                }
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Data explorer section
    st.header("Data Explorer")
    
    # Search bar
    search_term = st.text_input("Search for products", "")
    
    # Apply search filter
    if search_term:
        search_results = filtered_df[filtered_df['product'].str.contains(search_term, case=False)]
    else:
        search_results = filtered_df
    
    # Display data table with sort options
    st.dataframe(
        search_results,
        use_container_width=True,
        column_config={
            "company": st.column_config.TextColumn("Company"),
            "category": st.column_config.TextColumn("Category"),
            "product": st.column_config.TextColumn("Product"),
            "per_serve_size": st.column_config.TextColumn("Serving Size"),
            "energy_(kcal)": st.column_config.NumberColumn("Calories (kcal)", format="%.1f"),
            "carbohydrates_(g)": st.column_config.NumberColumn("Carbs (g)", format="%.1f"),
            "protein_(g)": st.column_config.NumberColumn("Protein (g)", format="%.1f"),
            "fiber_(g)": st.column_config.NumberColumn("Fiber (g)", format="%.1f"),
            "sugar_(g)": st.column_config.NumberColumn("Sugar (g)", format="%.1f"),
            "total_fat_(g)": st.column_config.NumberColumn("Total Fat (g)", format="%.1f"),
            "saturated_fat_(g)": st.column_config.NumberColumn("Saturated Fat (g)", format="%.1f"),
            "trans_fat_(g)": st.column_config.NumberColumn("Trans Fat (g)", format="%.1f"),
            "cholesterol_(mg)": st.column_config.NumberColumn("Cholesterol (mg)", format="%.1f"),
            "sodium_(mg)": st.column_config.NumberColumn("Sodium (mg)", format="%.1f")
        }
    )
    
    # Download button for filtered data
    csv = search_results.to_csv(index=False)
    st.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name="fast_food_nutrition_data.csv",
        mime="text/csv"
    )

    # Add prediction tab
    with tab4:
        st.subheader("Predict Nutritional Values")
    
        # Explanation
        st.markdown("""
        This model allows you to predict one nutritional value based on other values. 
        Select the target nutritional value you want to predict, then input the other values.
        """)
    
        # Select the target value to predict
        nutrition_cols = get_nutrition_columns(df)
        target_col = st.selectbox(
            "Select nutritional value to predict",
            options=nutrition_cols,
            index=0,
            key="pred_target"
        )
        
        # Build the prediction model
        model_data = build_prediction_model(df, target_col=target_col)
        
        # Display model metrics
        st.subheader(f"Model Performance ({model_data['model_name']})")
        metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
        
        with metrics_col1:
            st.metric("R² Score", f"{model_data['metrics']['r2']:.3f}")
        with metrics_col2:
            st.metric("RMSE", f"{model_data['metrics']['rmse']:.3f}")
        with metrics_col3:
            st.metric("MAE", f"{model_data['metrics']['mae']:.3f}")
        with metrics_col4:
            st.metric("MSE", f"{model_data['metrics']['mse']:.3f}")
        
        # Display feature importance if available
        if model_data['feature_importance'] is not None:
            # Sort features by importance
            sorted_features = sorted(
                model_data['feature_importance'].items(),
                key=lambda x: x[1],
                reverse=True
            )
            
            feature_names = [format_column_name(feat[0]) for feat in sorted_features]
            importance_values = [feat[1] for feat in sorted_features]
            
            fig = px.bar(
                x=importance_values,
                y=feature_names,
                orientation='h',
                title="Feature Importance",
                labels={'x': 'Importance', 'y': 'Feature'}
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Input form for prediction
        st.subheader("Enter Values for Prediction")
        
        # Create columns for input fields
        num_cols = 3
        input_fields = []
        
        # Split feature columns into rows of num_cols each
        feature_rows = [model_data['feature_cols'][i:i+num_cols] 
                        for i in range(0, len(model_data['feature_cols']), num_cols)]
        
        # Create input fields for each feature
        for row in feature_rows:
            cols = st.columns(num_cols)
            for i, feature in enumerate(row):
                with cols[i]:
                    # Get mean and std for the feature to suggest reasonable defaults
                    mean_val = df[feature].mean()
                    std_val = df[feature].std()
                    min_val = max(0, mean_val - 2*std_val)  # Prevent negative values
                    max_val = mean_val + 2*std_val
                    
                    # Create a slider with reasonable range
                    value = st.slider(
                        format_column_name(feature),
                        min_value=float(min_val),
                        max_value=float(max_val),
                        value=float(mean_val),
                        step=0.1
                    )
                    input_fields.append(value)
        
        # Predict button
        if st.button("Predict"):
            # Convert inputs to numpy array and reshape for prediction
            X_input = np.array(input_fields).reshape(1, -1)
            
            # Scale the input using the same scaler used for training
            X_input_scaled = model_data['scaler'].transform(X_input)
            
            # Make prediction
            prediction = model_data['model'].predict(X_input_scaled)[0]
            
            # Display prediction with appropriate formatting
            st.success(f"Predicted {format_column_name(target_col)}: **{prediction:.2f}**")
            
            # Find similar products in the dataset
            features_array = df[model_data['feature_cols']].values
            features_scaled = model_data['scaler'].transform(features_array)
            
            # Calculate distances to the input point
            distances = np.sqrt(np.sum((features_scaled - X_input_scaled)**2, axis=1))
            
            # Get top 5 similar products
            similar_indices = np.argsort(distances)[:5]
            similar_products = df.iloc[similar_indices]
            
            # Display similar products
            st.subheader("Similar Products")
            st.dataframe(
                similar_products[['company', 'category', 'product', target_col] + model_data['feature_cols']],
                use_container_width=True
            )

# Import needed for radar chart
import plotly.graph_objects as go
