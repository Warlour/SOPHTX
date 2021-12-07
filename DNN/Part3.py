import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale the data so that the values are from 0 - 1
x_train = x_train / 255
x_test = x_test / 255

# Flattening the train and test data
x_train_flattened = x_train.reshape(len(x_train), 28*28)
x_test_flattened = x_test.reshape(len(x_test), 28*28)

''' Bonus Content
Flattening data using keras Flatten class'''
model = keras.Sequential([
    keras.layers.Flatten(input_shape = (None, 28, 28)),
    keras.layers.Dense(100, activation = 'relu'),
    keras.layers.Dense(10, activation = 'sigmoid')
])

model.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

model.fit(x_train_flattened, y_train, epochs = 5)