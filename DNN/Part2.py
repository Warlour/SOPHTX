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

'''Part 2 - adding a hidden layer
Sequential create a stack of layers
Create a hidden layer with 100 neurons and relu activation'''
model = keras.Sequential([
    keras.layers.Dense(100, input_shape = (784,), activation = 'relu'),
    keras.layers.Dense(10, activation = 'sigmoid')
])

# Optimizer will help in backpropagration to reach better global optima
model.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

# Does the training
model.fit(x_train_flattened, y_train, epochs = 5)

# Evaluate the accuracy of the test set
model.evaluate(x_test_flattened, y_test)

# Using confusion matrix for validation
y_predicted = model.predict(x_test_flattened)
y_predicted_labels = [np.argmax(i) for i in y_predicted]

cm = tf.math.confusion_matrix(labels = y_test, predictions = y_predicted_labels)

import seaborn as sn
plt.figure(figsize = (10, 7))
sn.heatmap(cm, annot = True, fmt = 'd')
plt.xlabel('Predicted')
plt.ylabel('Truth')

plt.show()