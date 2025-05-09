from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import random

app = Flask(__name__)
CORS(app)

# Load ML model and label encoder
model = joblib.load("mood_predictor_model.pkl")
le = joblib.load("label_encoder.pkl")

# Load song dataset
df = pd.read_csv("enhanced_song_dataset.csv")

# Preprocess mood column
df['mood'] = df['mood'].astype(str).str.strip().str.lower().str.capitalize()

# Define feature columns (must match training order)
features = ['valence', 'danceability', 'energy', 'tempo', 'acousticness', 'liveness']

# Get unique moods
available_moods = sorted(df['mood'].dropna().unique().tolist())

@app.route("/api/moods", methods=["GET"])
def get_available_moods():
    """Return list of all available moods in the dataset."""
    return jsonify({"available_moods": available_moods})

@app.route("/api/recommend/mood", methods=["POST"])
def recommend_songs_by_mood():
    """Recommend songs based on selected mood."""
    data = request.get_json()
    mood_input = data.get("mood", "").strip().capitalize()

    if mood_input not in available_moods:
        return jsonify({"error": f"Mood '{mood_input}' not found."}), 404

    filtered_songs = df[df['mood'] == mood_input]

    if filtered_songs.empty:
        return jsonify({"error": f"No songs found for mood '{mood_input}'."}), 404

    count = min(random.randint(5, 8), len(filtered_songs))
    sampled_songs = filtered_songs.sample(count, random_state=42)

    return jsonify({
        "mood": mood_input,
        "songs": sampled_songs['song_name'].tolist()
    })

@app.route("/api/recommend/song", methods=["POST"])
def recommend_songs_by_song():
    """Recommend songs based on mood predicted from input song."""
    data = request.get_json()
    song_input = data.get("song", "").strip()

    if not song_input:
        return jsonify({"error": "Song name is required."}), 400

    song_row = df[df['song_name'].str.lower() == song_input.lower()]
    if song_row.empty:
        return jsonify({"error": f"Song '{song_input}' not found."}), 404

    try:
        # Build a single-row DataFrame with the correct feature names and order
        input_features = song_row[features].iloc[0].to_dict()
        input_df = pd.DataFrame([input_features], columns=features)

        predicted_mood_encoded = model.predict(input_df)[0]
        predicted_mood = le.inverse_transform([predicted_mood_encoded])[0].strip().capitalize()
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

    mood_songs = df[(
        df['mood'] == predicted_mood) & 
        (df['song_name'].str.lower() != song_input.lower())
    ]

    if mood_songs.empty:
        return jsonify({"error": f"No recommendations found for mood '{predicted_mood}'."}), 404

    count = min(random.randint(5, 8), len(mood_songs))
    recommendations = mood_songs.sample(count, random_state=42)

    return jsonify({
        "song_input": song_input,
        "predicted_mood": predicted_mood,
        "recommendations": recommendations['song_name'].tolist()
    })

if __name__ == "__main__":
    app.run(debug=True)
