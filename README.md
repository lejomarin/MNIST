# MNIST Digit Prediction App

## Overview

This project is a web-based application that uses a deep learning model to predict handwritten digits. The model is trained on the MNIST dataset and can predict digits from 0 to 9 with high accuracy. The application is built using Flask for the backend, HTML and JavaScript for the frontend, and is containerized using Docker for easy deployment and scalability.

The MNIST database of handwritten digits consists of float32 Numpy tensors of shapes:

(60000,784) for training (10000,784) for testing

The goal of the neural network is to accurately classify handwritten digits by minimizing the discrepancy between the predicted labels
and the true labels. This is achieved through the optimization process, in this case using variations of gradient descent algorithms. 
Mini-batch Stochastic Gradient Descent (SGD) is a commonly used optimization method for this purpose.

I determined the best hyperparameters for the model based on the sweeps performed in Weights and Biases.


<img width="872" alt="W B_chart" src="https://github.com/lejomarin/MNIST/assets/21342132/15d0c262-9514-4518-b9c8-431ab9b5432d">


## Features

**Digit Prediction:** Predicts handwritten digits using a Convolutional Neural Network (CNN).
**Web Interface:** Users can draw a digit on a canvas or upload an image, and the app will predict the digit.
**Docker Support:** The app is containerized with Docker, simplifying deployment and environment setup.

## Prerequisites
- Docker
- Python 3.8 or later
- A modern web browser

# Installation and Setup
## Clone the Repository

`git clone https://github.com/yourusername/mnist-digit-prediction-app.git`
`cd mnist-digit-prediction-app`

## Build the Docker Image

`docker build -t mnist-app .`

## Run the Docker Container

`docker run -p 5000:5000 mnist-app`

# Usage
Once the app is running, navigate to http://localhost:5000 in your web browser. Allow access to your camera. You will see an interface where you can take or upload a digit image. After submitting the digit, the model will predict and display the corresponding digit.

# Technologies Used
- **Flask:** Serves the web application and handles requests.
- **TensorFlow and Keras:** For building and training the deep learning model.
- **HTML/JavaScript:** For the frontend interface.
- **Docker:** For containerizing the application and simplifying deployment.
- **Weights & Biases:** For experiment tracking and visualization.

# Model Training

The deep learning model was trained using the MNIST dataset. The model architecture consists of convolutional layers followed by dense layers with ReLU activation functions. Training details, including hyperparameters and accuracy metrics, are tracked and visualized using Weights & Biases.

# Contributing
Contributions to the MNIST Digit Prediction App are welcome. Please follow the standard fork-branch-PR workflow.

## Tools used

- Keras
- Tensorflow
- Flask
- OpenCV
- Python
- HTML
- JavaScript
- JSON
