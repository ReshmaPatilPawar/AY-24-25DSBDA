import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from datetime import datetime

# Set page configuration with better aesthetics
st.set_page_config(
    page_title="COVID-19 Vaccination Dashboard - India",
    page_icon="💉",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Dataset Overview Section */
    .dataset-overview {
        background-color: #e3f2fd;  /* Light blue background */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 5px solid #1976d2;
    }
    
    /* First Dose Analysis Section */
    .first-dose {
        background-color: #e8f5e9;  /* Light green background */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 5px solid #388e3c;
    }
    
    /* Second Dose Analysis Section */
    .second-dose {
        background-color: #fff8e1;  /* Light amber background */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 5px solid #ffa000;
    }
    
    /* Gender-wise Analysis Section */
    .gender-analysis {
        background-color: #f3e5f5;  /* Light purple background */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 5px solid #8e24aa;
    }
    
    /* About This Dashboard Section */
    .about-dashboard {
        background-color: #e0f7fa;  /* Light cyan background */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 5px solid #00acc1;
    }
    
    /* Geographic Distribution Section */
    .geographic-dist {
        background-color: #ffebee;  /* Light red background */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 5px solid #d32f2f;
    }
    
    /* Section headers */
    .section-header {
        color: #2c3e50;
        padding-bottom: 10px;
        border-bottom: 2px solid #eee;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Load data with progress spinner
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/your_username/your_repo/main/covid_vaccine_statewise.csv"
    try:
        with st.spinner('Loading latest vaccination data...'):
            data = pd.read_csv(url)
            return data
    except:
        st.warning("Unable to fetch live data. Using sample data.")
        return pd.read_csv("covid_vaccine_statewise.csv")

df = load_data()

# Clean data - remove rows where State is India (aggregate)
df = df[df['State'] != 'India']

# Convert date column
df['Updated On'] = pd.to_datetime(df['Updated On'])
df['Date'] = df['Updated On'].dt.date

# Calculate additional metrics
df['Daily Doses'] = df.groupby('State')['Total Doses Administered'].diff().fillna(0)
df['Daily First Doses'] = df.groupby('State')['First Dose Administered'].diff().fillna(0)
df['Daily Second Doses'] = df.groupby('State')['Second Dose Administered'].diff().fillna(0)

# Title with better formatting
st.title("📊 COVID-19 Vaccination Analytics - India")
st.markdown("""
<div style="background-color:#3498db;padding:10px;border-radius:10px">
    <h3 style="color:white;text-align:center;">Tracking India's Vaccination Progress Against COVID-19</h3>
</div>
""", unsafe_allow_html=True)

# Sidebar filters with improved layout
st.sidebar.header("🔍 Filters")
selected_state = st.sidebar.selectbox("Select State", ['All States'] + sorted(df['State'].unique().tolist()))

min_date = df['Date'].min()
max_date = df['Date'].max()
date_range = st.sidebar.date_input(
    "Date Range", 
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Age group filter
age_groups = ['All Groups', '18-44', '45-60', '60+']
selected_age = st.sidebar.selectbox("Age Group", age_groups)

# Apply filters
if selected_state != 'All States':
    df_filtered = df[df['State'] == selected_state].copy()
else:
    df_filtered = df.copy()

df_filtered = df_filtered[
    (df_filtered['Date'] >= date_range[0]) & 
    (df_filtered['Date'] <= date_range[1])
]

# Main content with enhanced tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📋 Overview", 
    "💉 First Dose",
    "💉💉 Second Dose",
    "🚻 Gender Analysis",
    "📈 Trends",
    "🗺️ Geographic"
])

with tab1:
    st.header("📋 Dataset Overview")
    
    # Key metrics cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Total Vaccinations</h3>
            <h2>{:,}</h2>
        </div>
        """.format(df_filtered['Total Doses Administered'].max()), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>States Covered</h3>
            <h2>{}</h2>
        </div>
        """.format(df_filtered['State'].nunique()), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Time Period</h3>
            <h4>{} to {}</h4>
        </div>
        """.format(df_filtered['Date'].min().strftime('%b %d, %Y'), 
                  df_filtered['Date'].max().strftime('%b %d, %Y')), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive data explorer
    st.subheader("🔍 Data Explorer")
    st.dataframe(df_filtered.sort_values('Updated On', ascending=False).head(10), 
                height=300, use_container_width=True)
    
    # Download button
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Current Data",
        data=csv,
        file_name=f"covid_vaccine_data_{datetime.now().strftime('%Y%m%d')}.csv",
        mime='text/csv'
    )

with tab2:
    st.header("💉 First Dose Analysis")
    
    # Get latest first dose numbers by state
    latest_data = df_filtered.sort_values('Updated On').groupby('State').last().reset_index()
    
    # Metrics row
    col1, col2 = st.columns(2)
    with col1:
        total_first = latest_data['First Dose Administered'].sum()
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total First Doses Administered</h3>
            <h2>{total_first:,}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        avg_first = latest_data['First Dose Administered'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <h3>Average per State</h3>
            <h2>{avg_first:,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # Top/Bottom states
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏆 Top 10 States")
        top_first = latest_data.nlargest(10, 'First Dose Administered')[['State', 'First Dose Administered']]
        fig = px.bar(top_first, x='First Dose Administered', y='State', orientation='h',
                     color='First Dose Administered',
                     color_continuous_scale='Blues')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🐢 Bottom 10 States")
        bottom_first = latest_data.nsmallest(10, 'First Dose Administered')[['State', 'First Dose Administered']]
        fig = px.bar(bottom_first, x='First Dose Administered', y='State', orientation='h',
                     color='First Dose Administered',
                     color_continuous_scale='Reds')
        st.plotly_chart(fig, use_container_width=True)
    
    # State-wise comparison
    st.subheader("📊 State-wise Comparison")
    fig = px.bar(latest_data.sort_values('First Dose Administered', ascending=False),
                 x='State', y='First Dose Administered',
                 color='First Dose Administered',
                 color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("💉💉 Second Dose Analysis")
    
    # Get latest second dose numbers by state
    latest_data = df_filtered.sort_values('Updated On').groupby('State').last().reset_index()
    
    # Metrics row
    col1, col2 = st.columns(2)
    with col1:
        total_second = latest_data['Second Dose Administered'].sum()
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total Second Doses Administered</h3>
            <h2>{total_second:,}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        completion_rate = (total_second / total_first * 100) if total_first > 0 else 0
        st.markdown(f"""
        <div class="metric-card">
            <h3>Completion Rate</h3>
            <h2>{completion_rate:.1f}%</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # Top/Bottom states
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏆 Top 10 States")
        top_second = latest_data.nlargest(10, 'Second Dose Administered')[['State', 'Second Dose Administered']]
        fig = px.bar(top_second, x='Second Dose Administered', y='State', orientation='h',
                     color='Second Dose Administered',
                     color_continuous_scale='Greens')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🐢 Bottom 10 States")
        bottom_second = latest_data.nsmallest(10, 'Second Dose Administered')[['State', 'Second Dose Administered']]
        fig = px.bar(bottom_second, x='Second Dose Administered', y='State', orientation='h',
                     color='Second Dose Administered',
                     color_continuous_scale='Oranges')
        st.plotly_chart(fig, use_container_width=True)
    
    # Comparison with first dose
    st.subheader("📈 First vs Second Dose Comparison")
    comparison_df = latest_data[['State', 'First Dose Administered', 'Second Dose Administered']].melt(
        id_vars='State', var_name='Dose Type', value_name='Count')
    
    fig = px.bar(comparison_df, x='State', y='Count', color='Dose Type',
                 barmode='group', color_discrete_map={
                     'First Dose Administered': '#3498db',
                     'Second Dose Administered': '#2ecc71'
                 })
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.header("🚻 Gender-wise Analysis")
    
    # Get latest gender data by state
    latest_data = df_filtered.sort_values('Updated On').groupby('State').last().reset_index()
    
    # Calculate totals
    total_males = latest_data['Male (Doses Administered)'].sum()
    total_females = latest_data['Female (Doses Administered)'].sum()
    gender_ratio = (total_males / total_females) if total_females > 0 else 0
    
    # Metrics row
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>👨 Males Vaccinated</h3>
            <h2>{total_males:,}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>👩 Females Vaccinated</h3>
            <h2>{total_females:,}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>♂️/♀️ Ratio</h3>
            <h2>{gender_ratio:.2f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # Gender distribution by state
    st.subheader("📊 Gender Distribution by State")
    gender_df = latest_data[['State', 'Male (Doses Administered)', 'Female (Doses Administered)']].melt(
        id_vars='State', var_name='Gender', value_name='Count')
    
    fig = px.bar(gender_df, x='State', y='Count', color='Gender',
                 color_discrete_map={
                     'Male (Doses Administered)': '#3498db',
                     'Female (Doses Administered)': '#e74c3c'
                 })
    st.plotly_chart(fig, use_container_width=True)
    
    # Pie chart
    st.subheader("🍰 Overall Gender Distribution")
    fig = px.pie(names=['Male', 'Female'], 
                 values=[total_males, total_females],
                 color=['Male', 'Female'],
                 color_discrete_map={'Male':'#3498db', 'Female':'#e74c3c'})
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    st.header("📈 Vaccination Trends")
    
    # Time series data
    if selected_state == 'All States':
        ts_data = df_filtered.groupby('Date').agg({
            'Total Doses Administered': 'sum',
            'First Dose Administered': 'sum',
            'Second Dose Administered': 'sum',
            'Daily Doses': 'sum',
            'Daily First Doses': 'sum',
            'Daily Second Doses': 'sum'
        }).reset_index()
    else:
        ts_data = df_filtered.copy()
    
    # Daily vaccination trends
    st.subheader("📅 Daily Vaccination Trends")
    fig = px.line(ts_data, x='Date', y=['Daily First Doses', 'Daily Second Doses'],
                  labels={'value': 'Number of Vaccinations', 'variable': 'Dose Type'},
                  color_discrete_map={
                      'Daily First Doses': '#3498db',
                      'Daily Second Doses': '#2ecc71'
                  })
    st.plotly_chart(fig, use_container_width=True)
    
    # Cumulative trends
    st.subheader("📊 Cumulative Vaccination Progress")
    fig = px.area(ts_data, x='Date', y=['First Dose Administered', 'Second Dose Administered'],
                  labels={'value': 'Cumulative Vaccinations', 'variable': 'Dose Type'},
                  color_discrete_map={
                      'First Dose Administered': '#3498db',
                      'Second Dose Administered': '#2ecc71'
                  })
    st.plotly_chart(fig, use_container_width=True)
    
    # 7-day rolling average
    st.subheader("📉 7-Day Moving Average")
    ts_data['7DMA First'] = ts_data['Daily First Doses'].rolling(7).mean()
    ts_data['7DMA Second'] = ts_data['Daily Second Doses'].rolling(7).mean()
    
    fig = px.line(ts_data, x='Date', y=['7DMA First', '7DMA Second'],
                  labels={'value': '7-Day Average', 'variable': 'Dose Type'},
                  color_discrete_map={
                      '7DMA First': '#3498db',
                      '7DMA Second': '#2ecc71'
                  })
    st.plotly_chart(fig, use_container_width=True)

with tab6:
    st.header("🗺️ Geographic Distribution")
    
    # Load India geojson (simplified version)
    # Note: In a real implementation, you would need actual geojson data for Indian states
    try:
        india_geojson = "https://raw.githubusercontent.com/geohacker/india/master/state/india_state.geojson"
        
        # Prepare choropleth data
        latest_data = df_filtered.sort_values('Updated On').groupby('State').last().reset_index()
        
        # First dose map
        st.subheader("💉 First Dose Coverage")
        fig = px.choropleth(latest_data,
                            geojson=india_geojson,
                            locations='State',
                            featureidkey="properties.NAME_1",
                            color='First Dose Administered',
                            color_continuous_scale="Blues",
                            range_color=(0, latest_data['First Dose Administered'].max()),
                            labels={'First Dose Administered': 'First Doses Administered'}
                           )
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
        
        # Second dose map
        st.subheader("💉💉 Second Dose Coverage")
        fig = px.choropleth(latest_data,
                            geojson=india_geojson,
                            locations='State',
                            featureidkey="properties.NAME_1",
                            color='Second Dose Administered',
                            color_continuous_scale="Greens",
                            range_color=(0, latest_data['Second Dose Administered'].max()),
                            labels={'Second Dose Administered': 'Second Doses Administered'}
                           )
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.warning("Geographic visualization currently unavailable. Please check back later.")
        st.error(f"Error: {str(e)}")

# Dark theme version of About This Dashboard
st.markdown("""
<div style="
    background-color: #121212;  /* Dark background */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(255,255,255,0.1);
    border-left: 4px solid #1e88e5;  /* Bright blue accent */
    margin: 30px 0 0 0;
">
    <h4 style="
        color: #ffffff;  /* White text */
        padding-bottom: 8px;
        border-bottom: 1px solid #333333;
        margin-bottom: 12px;
        font-size: 1.1rem;
    ">About This Dashboard</h4>
    <p style="color: #e0e0e0; font-size: 0.95rem;">
        This interactive dashboard tracks India's COVID-19 vaccination progress across states and union territories.
    </p>
    <p style="color: #e0e0e0; font-size: 0.95rem;">
        <strong>Last Updated:</strong> {}
    </p>
    <p style="color: #e0e0e0; font-size: 0.95rem;">
        <strong>Data Source:</strong> 
        <a href="https://www.kaggle.com/sudalairajkumar/covid19-in-india" 
           target="_blank" 
           style="color: #82b1ff; text-decoration: none; font-weight: 500;">
           COVID-19 in India Dataset on Kaggle
        </a>
    </p>
</div>
""".format(datetime.now().strftime("%B %d, %Y %H:%M")), unsafe_allow_html=True)