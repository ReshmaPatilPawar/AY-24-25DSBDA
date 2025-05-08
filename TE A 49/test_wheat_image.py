import tensorflow as tf
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Set parameters
IMG_HEIGHT, IMG_WIDTH = 128, 128
MODEL_PATH = 'wheat_model.h5'

# Load the trained model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file {MODEL_PATH} not found. Please run train_wheat_model.py first.")
model = tf.keras.models.load_model(MODEL_PATH)
print(f"Model loaded from {MODEL_PATH}")

# Function to predict on a new image
def predict_wheat_image(image):
    img = image.resize((IMG_HEIGHT, IMG_WIDTH))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array, verbose=0)
    return "Healthy" if prediction[0][0] < 0.5 else "Unhealthy"

# Tkinter GUI
class WheatDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wheat Health Detection")
        self.root.geometry("400x200")

        # Label
        self.label = tk.Label(root, text="Select a wheat image to predict health status", font=("Arial", 12))
        self.label.pack(pady=10)

        # Browse button
        self.browse_button = tk.Button(root, text="Browse Image", command=self.browse_image, font=("Arial", 10))
        self.browse_button.pack(pady=10)

        # Prediction label
        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
        self.result_label.pack(pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
        if file_path:
            try:
                image = Image.open(file_path).convert('RGB')
                prediction = predict_wheat_image(image)
                self.result_label.config(text=f"Prediction: {prediction}", fg="green")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to process image: {str(e)}")

# Run the Tkinter app
if __name__ == '__main__':
    root = tk.Tk()
    app = WheatDetectionApp(root)
    root.mainloop()