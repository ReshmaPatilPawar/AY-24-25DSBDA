import pandas as pd

# Load the CSV file
movies_df = pd.read_csv('tmdb_5000_movies.csv')

# Print the first few rows to check column names
print(movies_df.head())

# Print all column names
print("Columns in CSV:", movies_df.columns)
