from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
import pandas as pd
from rapidfuzz import fuzz  # For fuzzy ingredient matching

# ----------------------------------------
# Initialize Flask App and Enable CORS
# ----------------------------------------
app = Flask(__name__)
CORS(app)  # Allow requests from different origins (e.g., frontend app)

# ----------------------------------------
# Load Model, Vectorizer, and Dataset
# ----------------------------------------
model_path = os.path.join('model', 'recipe_model.pkl')
vectorizer_path = os.path.join('model', 'vectorizer.pkl')
data_path = 'recipe.csv'

# Load trained ML model and TF-IDF vectorizer
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Load dataset and drop rows with missing values
df = pd.read_csv(data_path).dropna()

# ----------------------------------------
# Function to Find Matching Recipes Using Fuzzy Matching
# ----------------------------------------
def get_all_matching_recipes(ingredients_input, df, threshold=80):
    """
    Fuzzy match user ingredients with recipe ingredients using RapidFuzz.
    Returns all recipes with at least one fuzzy-matched ingredient.
    """
    input_ingredients = [ing.strip().lower() for ing in ingredients_input.split(',')]
    matches = []

    for _, row in df.iterrows():
        recipe_ingredients = [ing.strip().lower() for ing in row['Ingredients'].split(',')]
        matched = []

        for user_ing in input_ingredients:
            for recipe_ing in recipe_ingredients:
                if fuzz.partial_ratio(user_ing, recipe_ing) >= threshold:
                    matched.append(recipe_ing)
                    break  # Avoid duplicate matching

        if matched:
            matches.append({
                'Category': row['Category'],
                'Cuisine': row['Cuisine'],
                'MatchedIngredients': list(set(matched)),
                'AllIngredients': recipe_ingredients
            })

    # Sort by number of matched ingredients (most relevant first)
    matches.sort(key=lambda x: len(x['MatchedIngredients']), reverse=True)
    return matches

# ----------------------------------------
# API Route to Handle Recipe Prediction
# ----------------------------------------
@app.route('/predict', methods=['POST'])
def predict():
    """
    Handles prediction request.
    1. First attempts to find matches in dataset based on input ingredients.
    2. If no matches found, uses ML model to predict Category and Cuisine.
    """
    data = request.get_json()
    ingredients = data.get('ingredients', '').strip()

    if not ingredients:
        return jsonify({'error': 'No ingredients provided'}), 400

    # Step 1: Try to find recipes with matching ingredients using fuzzy match
    matches = get_all_matching_recipes(ingredients, df)
    if matches:
        return jsonify({
            'source': 'dataset',
            'matches': matches
        })

    # Step 2: Check if any of the input ingredients are known (loosely)
    input_ingredients = set(ingredients.lower().strip().split(','))
    known_ingredients = set()
    for row in df['Ingredients']:
        known_ingredients |= set(i.strip().lower() for i in row.split(','))

    if not input_ingredients & known_ingredients:
        # If none of the ingredients are known, prediction is unreliable
        return jsonify({
            'source': 'model',
            'Category': 'Unknown',
            'Cuisine': 'Unknown'
        })

    # Step 3: Predict using ML model
    vectorized = vectorizer.transform([ingredients])
    prediction = model.predict(vectorized)

    return jsonify({
        'source': 'model',
        'Category': prediction[0][0],
        'Cuisine': prediction[0][1]
    })

# ----------------------------------------
# Run Flask App
# ----------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
