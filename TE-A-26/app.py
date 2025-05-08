from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and scaler
model = joblib.load('movie_revenue_rf_model.pkl')
scaler = joblib.load('scaler.pkl')

# Define top genres
top_genres = ['Drama', 'Comedy', 'Thriller', 'Action', 'Adventure']


@app.route('/')
def home():
    """Serve the prediction form."""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Predict movie revenue based on input features."""
    try:
        # Get JSON data
        data = request.get_json()

        # Extract features with defaults
        budget = float(data.get('budget', 0))
        runtime = float(data.get('runtime', 0))
        popularity = float(data.get('popularity', 0))
        vote_average = float(data.get('vote_average', 0))
        vote_count = float(data.get('vote_count', 0))
        release_year = float(data.get('release_year', 0))
        genres = data.get('genres', [])

        # Ensure genres is a list
        genres = [genres] if isinstance(genres, str) and genres else [
        ] if not isinstance(genres, list) else genres

        # Create genre features
        genre_features = {
            f'genre_{g}': 1 if g in genres else 0 for g in top_genres}

        # Build feature array
        feature_names = ['budget', 'runtime', 'popularity', 'vote_average',
                         'vote_count', 'release_year'] + [f'genre_{g}' for g in top_genres]
        features = [budget, runtime, popularity, vote_average, vote_count,
                    release_year] + [genre_features[f'genre_{g}'] for g in top_genres]

        # Convert to DataFrame
        input_df = pd.DataFrame([features], columns=feature_names)

        # Scale and predict
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)[0]

        return jsonify({
            'status': 'success',
            'predicted_revenue': round(prediction, 2)
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400


@app.route('/favicon.ico')
def favicon():
    """Handle favicon requests."""
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
