from flask import Flask, request, jsonify
import base64
import numpy as np
from tensorflow.keras.models import load_model
from flask_cors import CORS
from PIL import Image
from PIL import ImageOps
import io
import os
import cv2

app = Flask(__name__)
CORS(app)

model = load_model('MNIST_model_Feb_24.h5')  # Load your trained model

@app.route('/')
def index():
    return "MNIST Digit Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the POST request
    image_data = request.json['image']

    # Process the image data
    response = process_image(image_data)

    return jsonify(response)

def process_image(image_data):
    # Decode the image data from base64
    image_bytes = base64.b64decode(image_data.split(",")[1])
    image = Image.open(io.BytesIO(image_bytes))

    # Convert the image to grayscale
    image = image.convert('L')

    # Resize the image to 28x28 pixels
    image = image.resize((28, 28))
    
    # Convert the image to a numpy array
    image_np = np.array(image)
    
    threshold_value = 118
    # Apply threshold to convert the image to strictly black and white
    # and invert the colors
    _, image_bw_inverted = cv2.threshold(image_np, threshold_value, 255, cv2.THRESH_BINARY_INV)

    # Convert back to PIL image to use the existing saving mechanism
    image = Image.fromarray(image_bw_inverted)

    
    # Relative path to an 'images' directory in the same location as your Flask app
    save_path = os.path.join(os.getcwd(), 'images')

    file_name = 'processed_image.jpg'
    full_path = os.path.join(save_path, file_name)

    # Debugging prints
    print(f"Saving image to: {full_path}")
    if not os.path.exists(save_path):
        print(f"Creating directory: {save_path}")
        os.makedirs(save_path)

    # Save the image
    image.save(full_path)
    print(f"Image saved successfully to {full_path}")
    
    # Normalize and prepare image for model
    image_array = image_bw_inverted.astype('float32') / 255.0
    image_array = image_array.reshape(1, 28 * 28)  # Flatten the image


    # Make a prediction
    prediction = model.predict(image_array)
    digit = np.argmax(prediction)

    # Prepare the response
    response = {'digit': int(digit)}
    return response

if __name__ == '__main__':
    app.run(debug=True)
