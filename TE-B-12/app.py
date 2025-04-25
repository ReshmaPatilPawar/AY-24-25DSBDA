import streamlit as st
import pandas as pd
import requests
import scipy.sparse

TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"  # Your API key

# 🔹 Function to fetch the TMDB Movie ID dynamically
def get_movie_id(movie_name):
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_name}"
    response = requests.get(search_url).json()
    
    if response["results"]:
        return response["results"][0]["id"]  # Get the first movie ID
    return None  # Return None if no movie found

# 🔹 Function to fetch the poster using TMDB Movie ID
def fetch_poster(movie_name):
    movie_id = get_movie_id(movie_name)  # Get the correct TMDB movie ID
    
    if movie_id:
        movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
        data = requests.get(movie_url).json()
        
        if "poster_path" in data and data["poster_path"]:
            return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    
    print(f"No valid poster found for: {movie_name}")  # Debugging message
    return "https://image.tmdb.org/t/p/w500/default_poster_path.jpg"  # Default image

# 🔹 Load movie dataset
movies_df = pd.read_csv("IMDB_Top_250_Movies.csv")  # Load movie dataset

# 🔹 Load similarity matrix
similarity = scipy.sparse.load_npz("similarity.npz")

# 🔹 Recommendation function
def recommend(movie_name):
    if movie_name not in movies_df["name"].values:
        return [], []

    movie_index = movies_df[movies_df["name"] == movie_name].index[0]
    distances = similarity[movie_index].toarray().flatten()
    similar_movies = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = []
    recommended_posters = []
    
    for idx, _ in similar_movies:
        movie_title = movies_df.iloc[idx]["name"]  # Get movie name
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_title))  # Fetch poster by name
    
    return recommended_movies, recommended_posters

# 🔹 Streamlit UI
st.title("Movie Recommender System")

selected_movie_name = st.selectbox("Select a movie:", movies_df["name"].values)

if st.button("Recommend"):
    recommended_names, recommended_posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.write(recommended_names[i])  # Display movie name
            st.image(recommended_posters[i], use_container_width=True)


