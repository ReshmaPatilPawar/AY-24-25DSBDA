from flask import Flask, render_template, request
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import numpy as np

app = Flask(__name__)

# Check for required libraries
try:
    from flask import Flask, render_template, request
except ImportError as e:
    print("Error: Flask is not installed. Please install it using 'pip install flask'.")
    exit(1)

try:
    import pandas as pd
except ImportError as e:
    print("Error: pandas is not installed. Please install it using 'pip install pandas'.")
    exit(1)

try:
    from scipy import stats
except ImportError as e:
    print("Error: scipy is not installed. Please install it using 'pip install scipy'.")
    exit(1)

try:
    from sklearn.linear_model import LinearRegression
    from sklearn.impute import SimpleImputer
except ImportError as e:
    print("Error: scikit-learn is not installed. Please install it using 'pip install scikit-learn'.")
    exit(1)

# Load and clean the dataset
try:
    df = pd.read_csv("https://raw.githubusercontent.com/krishna-koly/IMDB_TOP_1000/main/imdb_top_1000.csv")
    df.columns = [col.lower().strip() for col in df.columns]
    if df.columns.duplicated().any():
        raise ValueError("Duplicate column names detected in DataFrame")
    df['runtime'] = df['runtime'].str.extract(r'(\d+)').astype(float)
    df['gross'] = df['gross'].str.replace(',', '', regex=True).astype(float)
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit(1)

# Prepare data for regression
try:
    # Select features and target
    features = ['runtime', 'gross', 'no_of_votes']
    target = 'imdb_rating'
    
    # Create a copy of the dataset for regression
    df_reg = df[features + [target]].dropna()
    
    # Handle missing values using SimpleImputer (though dropna already removes them)
    imputer = SimpleImputer(strategy='mean')
    X = imputer.fit_transform(df_reg[features])
    y = df_reg[target]
    
    # Train the regression model
    reg_model = LinearRegression()
    reg_model.fit(X, y)
except Exception as e:
    print(f"Error training regression model: {e}")
    exit(1)

def top_movies_by_genre(genre, df, top_n=5, sort_by='imdb_rating', sort_order='descending'):
    try:
        df['genre'] = df['genre'].str.lower()
        filtered = df[df['genre'].str.split(', ').apply(lambda x: any(genre.lower() in g for g in x))]
        if filtered.empty:
            return None
        valid_sort_cols = ['imdb_rating', 'runtime', 'gross', 'no_of_votes']
        if sort_by not in valid_sort_cols:
            sort_by = 'imdb_rating'
        if sort_order == 'ascending':
            return filtered.sort_values(by=sort_by, ascending=True).head(top_n)[['series_title', 'genre', 'imdb_rating', 'runtime', 'gross', 'no_of_votes']]
        else:
            return filtered.sort_values(by=sort_by, ascending=False).head(top_n)[['series_title', 'genre', 'imdb_rating', 'runtime', 'gross', 'no_of_votes']]
    except Exception as e:
        print(f"Error in top_movies_by_genre: {e}")
        return None

def predict_rating(runtime, gross, votes):
    try:
        # Prepare input data for prediction
        input_data = np.array([[runtime, gross, votes]])
        
        # Impute missing values if any (though inputs should be valid)
        input_data = imputer.transform(input_data)
        
        # Predict using the trained model
        prediction = reg_model.predict(input_data)[0]
        
        # Ensure prediction is within a reasonable range (e.g., 0 to 10 for IMDb ratings)
        prediction = max(0, min(10, prediction))
        return round(prediction, 2)
    except Exception as e:
        print(f"Error in prediction: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/overview')
def overview():
    try:
        shape = df.shape
        columns = df.columns.tolist()
        dtypes = df.dtypes.to_dict()
        return render_template('overview.html', rows=shape[0], cols=shape[1], columns=columns, dtypes=dtypes)
    except Exception as e:
        return render_template('error.html', error=f"Error generating overview: {str(e)}")

@app.route('/statistics')
def statistics():
    try:
        stats = df.describe(include='all').T[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']].to_dict()
        unique_values = {
            'series_title': df['series_title'].nunique(),
            ' Dış: df['director'].nunique(),
            'genres': df['genre'].nunique()
        }
        return render_template('statistics.html', stats=stats, unique_values=unique_values)
    except Exception as e:
        return render_template('error.html', error=f"Error generating statistics: {str(e)}")

@app.route('/genre', methods=['GET', 'POST'])
def genre():
    movies = None
    genre_input = ''
    top_n = 5
    sort_by = 'imdb_rating'
    sort_order = 'descending'
    genre_options = ['Action', 'Comedy', 'Drama', 'Horror', 'Adventure']
    sort_options = ['descending', 'ascending']
    sort_by_options = ['imdb_rating', 'runtime', 'gross', 'no_of_votes']
    prediction = None
    pred_error = None

    try:
        if request.method == 'POST':
            genre_input = request.form.get('genre', '').strip()
            try:
                top_n = int(request.form.get('top_n', 5))
                if top_n < 1 or top_n > 10:
                    top_n = 5
            except ValueError:
                top_n = 5
            sort_by = request.form.get('sort_by', 'imdb_rating')
            sort_order = request.form.get('sort_order', 'descending')
            print(f"Genre: {genre_input}, Top N: {top_n}, Sort By: {sort_by}, Sort Order: {sort_order}")
            if genre_input in genre_options:
                movies = top_movies_by_genre(genre_input, df, top_n, sort_by, sort_order)
                print(f"Movies retrieved: {movies.shape if movies is not None else 'None'}")

            if request.form.get('predict'):
                try:
                    runtime = float(request.form.get('pred_runtime', 0))
                    gross = float(request.form.get('pred_gross', 0))
                    votes = float(request.form.get('pred_votes', 0))
                    print(f"Prediction inputs - Runtime: {runtime}, Gross: {gross}, Votes: {votes}")
                    prediction = predict_rating(runtime, gross, votes)
                    if prediction is None:
                        pred_error = "Prediction failed. Please check input values."
                except ValueError:
                    pred_error = "Invalid input for prediction. Please enter numeric values."

        return render_template('genre.html', movies=movies, genre_input=genre_input, top_n=top_n, genre_options=genre_options, sort_order=sort_order, sort_options=sort_options, sort_by=sort_by, sort_by_options=sort_by_options, prediction=prediction, pred_error=pred_error)
    except Exception as e:
        return render_template('error.html', error=f"Error processing genre search: {str(e)}")

@app.route('/hypothesis')
def hypothesis():
    try:
        action_movies = df[df['genre'].str.contains('Action', case=False, na=False)]
        comedy_movies = df[df['genre'].str.contains('Comedy', case=False, na=False)]
        action_budgets = action_movies['gross'].dropna()
        comedy_budgets = comedy_movies['gross'].dropna()
        if len(action_budgets) < 2 or len(comedy_budgets) < 2:
            raise ValueError("Insufficient data for t-test")
        t_statistic, p_value = stats.ttest_ind(action_budgets, comedy_budgets, nan_policy='omit')
        result = {
            't_statistic': round(t_statistic, 2),
            'p_value': round(p_value, 3),
            'significant': p_value < 0.05
        }
        return render_template('hypothesis.html', result=result)
    except Exception as e:
        return render_template('error.html', error=f"Error generating hypothesis: {str(e)}")

@app.route('/charts')
def charts():
    return render_template('charts.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
