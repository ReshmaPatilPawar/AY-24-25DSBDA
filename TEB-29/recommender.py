# recommender.py

class MovieGenreRecommender:
    def __init__(self, df, vectorizer, kmeans):
        self.df = df
        self.vectorizer = vectorizer
        self.kmeans = kmeans

    def recommend_by_genre(self, genre, n=10):
        genre = genre.lower()
        return self.df[self.df['genre_str'].str.lower().str.contains(genre)]['title'].head(n).tolist()

    def recommend_by_cluster(self, genre, n=10):
        test_vec = self.vectorizer.transform([genre])
        cluster = self.kmeans.predict(test_vec)[0]
        return self.df[self.df['cluster'] == cluster]['title'].head(n).tolist()
