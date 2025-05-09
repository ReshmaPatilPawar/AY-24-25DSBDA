import pandas as pd
import joblib
import random

# Load model and label encoder
model = joblib.load("mood_predictor_model.pkl")
le = joblib.load("label_encoder.pkl")

# Load dataset
df = pd.read_csv("enhanced_song_dataset.csv")

# Clean mood column
df['mood'] = df['mood'].astype(str).str.strip().str.lower().str.capitalize()

# Get unique moods
available_moods = sorted(df['mood'].dropna().unique().tolist())
available_moods_lower = [m.lower() for m in available_moods]

# Features for prediction (must match training!)
features = ['valence', 'danceability', 'energy', 'tempo', 'acousticness', 'liveness']

# Load saved features list
saved_features = joblib.load("model_features.pkl")

# Check if the feature order is correct
if saved_features != features:
    raise ValueError("Feature mismatch: The order of features does not match the model's training features.")

# Recommend songs based on mood
def get_top_songs_by_mood(mood_input):
    mood_input = mood_input.strip().lower().capitalize()
    if mood_input not in df['mood'].values:
        return f"[❌] Mood '{mood_input}' not found."

    count = random.randint(5, 8)
    top_songs = df[df['mood'] == mood_input].sample(min(count, len(df)), random_state=42)
    result = f"[🎧] {len(top_songs)} songs for mood '{mood_input}':\n"
    result += "\n".join([f"{i+1}. {song}" for i, song in enumerate(top_songs['song_name'].values)])
    return result

# Recommend songs based on a song name
def get_top_songs_by_song_name(song_input):
    song_row = df[df['song_name'].str.lower() == song_input.lower()]
    if song_row.empty:
        return f"[❌] Song '{song_input}' not found."

    try:
        # Ensure correct feature format and order
        input_features_dict = song_row[features].iloc[0].to_dict()
        input_df = pd.DataFrame([input_features_dict], columns=features)

        predicted_mood_encoded = model.predict(input_df)[0]
        predicted_mood = le.inverse_transform([predicted_mood_encoded])[0].strip().capitalize()
    except Exception as e:
        return f"[❌] Prediction failed: {str(e)}"

    mood_matches = df[(df['mood'] == predicted_mood) & 
                      (df['song_name'].str.lower() != song_input.lower())]

    if mood_matches.empty:
        return f"[❌] No songs found for mood '{predicted_mood}'."

    count = random.randint(5, 8)
    recommended = mood_matches.sample(min(count, len(mood_matches)), random_state=42)
    result = f"[🎧] Song '{song_input}' is in '{predicted_mood}' mood.\n"
    result += f"Here are {len(recommended)} recommended songs with the same mood:\n"
    result += "\n".join([f"{i+1}. {song}" for i, song in enumerate(recommended['song_name'].values)])
    return result

# Show available moods
print("Available moods:", ", ".join(available_moods))

# Input from user
user_input = input(f"\nEnter a mood ({', '.join(available_moods)}) or a song name: ").strip()

# Recommend based on mood or song
if user_input.lower().capitalize() in available_moods:
    print(get_top_songs_by_mood(user_input))
else:
    print(get_top_songs_by_song_name(user_input))
