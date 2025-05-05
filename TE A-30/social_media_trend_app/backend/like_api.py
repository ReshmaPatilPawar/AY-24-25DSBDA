# backend/like_api.py
from flask import Flask, jsonify
import pandas as pd

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

from sklearn.linear_model import LinearRegression

# app = Flask(__name__)

EXCEL_PATH = "../public/Social_Media_Trends.xlsx"

@app.route("/like_post/<int:post_id>", methods=["POST"])
def like_post(post_id):
    try:
        print("Post ID:", post_id)
        
        df = pd.read_excel(EXCEL_PATH)
        print(f"Liking post with ID: {post_id}")
        
        if post_id < 0 or post_id >= len(df):
            return jsonify({"status": "error", "message": "Invalid post ID"})

        df.at[post_id, 'Likes'] += 1
        df.to_excel(EXCEL_PATH, index=False)

        return jsonify({"status": "success", "likes": int(df.at[post_id, 'Likes'])})
    
    except Exception as e:
        print("Error in like_post:", e)
        return jsonify({"error": str(e)}), 500
    
@app.route("/predict_likes/<int:retweets>", methods=["GET"])
def predict_likes(retweets):
    try:
        df = pd.read_excel(EXCEL_PATH)
        X = df[['Retweets']]
        y = df['Likes']

        model = LinearRegression()
        model.fit(X, y)

        predicted_likes = model.predict([[retweets]])[0]

        return jsonify({"retweets": retweets, "predicted_likes": round(predicted_likes)})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
