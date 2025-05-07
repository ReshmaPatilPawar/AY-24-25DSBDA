from flask import Flask, request, jsonify, render_template_string
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

app = Flask(__name__)
model = load_model("age_gender_model.h5", compile=False)

# HTML template
HTML_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Age & Gender Predictor</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center">
    <div class="bg-white shadow-xl rounded-2xl p-8 max-w-md w-full animate-fade-in">
        <h1 class="text-2xl font-semibold text-gray-800 mb-6 text-center">Upload a Face Image</h1>
        <form method="POST" action="/predict" enctype="multipart/form-data" class="flex flex-col items-center gap-4">
            <input type="file" name="image" id="imageInput" accept="image/*" required
                   class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4
                          file:rounded-full file:border-0 file:text-sm file:font-semibold
                          file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"/>
            <img id="preview" src="#" alt="Preview" class="mt-4 max-w-xs rounded-lg hidden shadow-lg" />
            <button type="submit"
                    class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-6 rounded-full transition">
                Predict
            </button>
        </form>

        {% if prediction %}
        <div class="mt-6 text-center">
            <p class="text-gray-700 text-lg"><strong>Age:</strong> {{ prediction.age }}</p>
            <p class="text-gray-700 text-lg"><strong>Gender:</strong> {{ prediction.gender }}</p>
        </div>
        {% endif %}
    </div>

    <script>
        const imageInput = document.getElementById('imageInput');
        const preview = document.getElementById('preview');

        imageInput.addEventListener('change', function () {
            const file = this.files[0];
            if (file) {
                preview.src = URL.createObjectURL(file);
                preview.classList.remove("hidden");
            }
        });
    </script>
</body>
</html>
'''


def preprocess_image(image, target_size=(64, 64)):
    image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, target_size)
    image = image.astype(np.float32) / 255.0
    return np.expand_dims(image, axis=0)

@app.route('/', methods=['GET'])
def home():
    return render_template_string(HTML_PAGE)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    image = preprocess_image(image_file)
    
    age_pred, gender_pred = model.predict(image)
    predicted_age = int(age_pred[0][0])
    predicted_gender = 'Male' if gender_pred[0][0] < 0.5 else 'Female'

    return render_template_string(HTML_PAGE, prediction={
        'age': predicted_age,
        'gender': predicted_gender
    })

if __name__ == '__main__':
    app.run(debug=True, port=5050)
