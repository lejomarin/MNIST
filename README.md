handwritten digit prediction using neural networks The MNIST database of handwritten digits consists of float32 Numpy tensors of shapes:

(60000,784) for training (10000,784) for testing

The goal of the neural network is to accurately classify handwritten digits by minimizing the discrepancy between the predicted labels
and the true labels. This is achieved through the optimization process, in this case using variations of gradient descent algorithms. 
Mini-batch Stochastic Gradient Descent (SGD) is a commonly used optimization method for this purpose.

