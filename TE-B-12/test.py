import pandas as pd

# Load movies dataset
movies = pd.read_csv("movies.csv")

# Check the first few rows of the "genres" column
print(movies["genres"].head(10))
