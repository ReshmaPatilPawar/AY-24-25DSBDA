from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pickle
import re
import urllib.parse

app = Flask(__name__)

# Load model, scaler, and dataset
try:
    with open('model/music_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('model/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    df = pd.read_csv("model/dataset.csv")
except FileNotFoundError:
    raise Exception("❌ Required files not found.")

# Clean text
def clean_text(text):
    text = str(text).lower()
    return re.sub(r'[^a-z0-9\s]', '', text)

# Generate YouTube search link
def generate_youtube_link(song_title):
    query = urllib.parse.quote(song_title + " official video")
    return f"https://www.youtube.com/results?search_query={query}"

# Recommend songs based on input title
def recommend(song_title):
    song_index = df[df['track_name'].str.lower() == song_title.lower()].index
    if len(song_index) == 0:
        return []
    song_index = song_index[0]
    X = df[['danceability', 'energy']]
    distances, indices = model.kneighbors([X.iloc[song_index]], n_neighbors=6)

    recommendations = []
    recommended_titles = set()
    for i in indices[0][1:]:
        rec_song = df.iloc[i]
        title = rec_song['track_name']
        if title not in recommended_titles:
            recommended_titles.add(title)
            recommendations.append({
                'title': title,
                'artists': rec_song['artists'],
                'popularity': rec_song['popularity'],
                'danceability': rec_song['danceability'],
                'energy': rec_song['energy'],
                'youtube_link': generate_youtube_link(title)
            })
    return recommendations

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    song = request.form['song']
    recommendations = recommend(song)
    return render_template('index.html', song=song, recommendations=recommendations)

@app.route('/suggest')
def suggest():
    query = request.args.get('song', '').lower()
    suggestions = df[df['track_name'].str.lower().str.contains(query, na=False)]['track_name'].unique().tolist()
    return jsonify({'suggestions': suggestions[:10]})

if __name__ == '__main__':
    app.run(debug=True)
