import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Set page configuration
st.set_page_config(
    page_title="Cricket Performance Predictor",
    page_icon="🏏",
    layout="wide"
)

# Custom CSS for style
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .title {
        text-align: center;
        color: #1a73e8;
    }
    .subtitle {
        color: #6c757d;
    }
    .dataframe th {
        background-color: #007bff !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("cricket_data_2025.csv")
    df.replace("No stats", pd.NA, inplace=True)
    numeric_cols = [
        "Year", "Matches_Batted", "Not_Outs", "Runs_Scored", "Balls_Faced",
        "Batting_Average", "Batting_Strike_Rate", "Centuries", "Half_Centuries",
        "Fours", "Sixes", "Catches_Taken", "Stumpings", "Matches_Bowled",
        "Balls_Bowled", "Runs_Conceded", "Wickets_Taken", "Bowling_Average",
        "Economy_Rate", "Bowling_Strike_Rate", "Four_Wicket_Hauls", "Five_Wicket_Hauls"
    ]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
    return df

def train_and_predict(df):
    batting_features = [
        "Matches_Batted", "Not_Outs", "Balls_Faced", "Batting_Strike_Rate",
        "Centuries", "Half_Centuries", "Fours", "Sixes"
    ]
    batting_target = "Runs_Scored"
    
    df_batting = df.dropna(subset=batting_features + [batting_target])
    train_data = df_batting[df_batting["Year"] < 2024]
    test_data = df_batting[df_batting["Year"] == 2024]

    X_train, X_test = train_data[batting_features], test_data[batting_features]
    y_train, y_test = train_data[batting_target], test_data[batting_target]
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    
    future_2025 = test_data.copy()
    future_2025["Year"] = 2025
    future_2025["Predicted_Runs"] = model.predict(future_2025[batting_features])
    
    return model, future_2025, mae

# --------------------------- Streamlit UI --------------------------- #

st.title("🏏 Cricket Player Performance Predictor")
st.markdown("##### 🧠 Predicting player **Runs for 2025** using machine learning (Random Forest)")
st.divider()

# Load and preview data
df = load_data()
st.success("✅ Dataset loaded successfully!")

st.subheader("📄 Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)
st.divider()

# Train model and show results
st.subheader("⚙️ Model Training & Prediction")
model, future_predictions, mae = train_and_predict(df)
st.markdown(f"📉 **Model Mean Absolute Error (MAE):** `{mae:.2f}` runs")

st.subheader("🔮 Predicted Runs for 2025 (Top 10)")
st.dataframe(future_predictions[["Player_Name", "Year", "Predicted_Runs"]].sort_values(
    by="Predicted_Runs", ascending=False).head(10), use_container_width=True)

st.divider()

# Visualization
st.subheader("📊 Runs Distribution (Actual Runs)")
fig, ax = plt.subplots()
df["Runs_Scored"].dropna().hist(bins=25, ax=ax, color='lightgreen', edgecolor='black')
ax.set_xlabel("Runs Scored")
ax.set_ylabel("Number of Players")
ax.set_title("Distribution of Runs Scored")
st.pyplot(fig)

# Optional Plotly chart
st.subheader("📈 Interactive Chart: Predicted Runs 2025")
plot_df = future_predictions[["Player_Name", "Predicted_Runs"]].sort_values(by="Predicted_Runs", ascending=False).head(15)
fig_plotly = px.bar(plot_df, x="Predicted_Runs", y="Player_Name", orientation="h",
                    color="Predicted_Runs", color_continuous_scale="Viridis", title="Top 15 Predicted Scorers")
fig_plotly.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig_plotly, use_container_width=True)

st.divider()

# Predict for specific player
st.subheader("🔎 Search Player Prediction")
player = st.selectbox("Select a player to view prediction", future_predictions["Player_Name"].unique())
player_data = future_predictions[future_predictions["Player_Name"] == player]

if not player_data.empty:
    st.markdown(f"### 📌 Predicted Runs for **{player}** in 2025: `{int(player_data['Predicted_Runs'].values[0])} runs`")
    st.dataframe(player_data[["Year", "Matches_Batted", "Balls_Faced", "Predicted_Runs"]], use_container_width=True)
