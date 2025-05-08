from flask import Flask, request, render_template_string
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load dataset directly from the online source
df = pd.read_csv("https://raw.githubusercontent.com/rashida048/Some-NLP-Projects/master/movie_dataset.csv")
features = ['keywords', 'cast', 'genres', 'director']

for feature in features:
    df[feature] = df[feature].fillna('')

def combine_features(row):
    return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']

df["combined_features"] = df.apply(combine_features, axis=1)
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    try:
        return df[df.title.str.lower() == title.lower()]["index"].values[0]
    except:
        return None

# HTML templates using render_template_string
home_html = '''
<!DOCTYPE html>
<html>
<head><title>Movie Recommender</title></head>
<body style="font-family:Arial; text-align:center;">
    <h2>Movie Recommendation System</h2>
    <form method="POST" action="/recommend">
        <input type="text" name="movie" placeholder="Enter a movie name" required>
        <br><br>
        <button type="submit">Get Recommendations</button>
    </form>
</body>
</html>
'''

result_html = '''
<!DOCTYPE html>
<html>
<head><title>Recommendations</title></head>
<body style="font-family:Arial; text-align:center;">
    <h2>Top 5 movies similar to "{{ movie_name }}"</h2>
    <ul>
    {% for movie in recommendations %}
        <li>{{ movie }}</li>
    {% endfor %}
    </ul>
    <br><a href="/">Back</a>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(home_html)

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie']
    try:
        movie_index = get_index_from_title(movie_name)
        if movie_index is None:
            raise ValueError("Movie not found.")
        similar_movies = list(enumerate(cosine_sim[movie_index]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:6]
        recommendations = [get_title_from_index(element[0]) for element in sorted_similar_movies]
        return render_template_string(result_html, movie_name=movie_name, recommendations=recommendations)
    except:
        return render_template_string("<h3>Movie not found. Please try again. <a href='/'>Go back</a></h3>")

if __name__ == '__main__':
    app.run(debug=True)
