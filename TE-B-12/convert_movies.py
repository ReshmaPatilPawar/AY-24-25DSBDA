import pandas as pd

# Load the existing movies.pkl file
df = pd.read_pickle("movies.pkl")

# Save as CSV (Recommended for Streamlit)
df.to_csv("movies.csv", index=False)

# Save as JSON (Alternative)
df.to_json("movies.json", orient="records")

print("Conversion complete! Now use movies.csv or movies.json in your Streamlit app.")
