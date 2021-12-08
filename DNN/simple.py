import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt
import numpy as np

image = int(input("Insert random number from 0-9999: "))
if (image > 9999 or image < 0):
    raise ValueError("Image index is too high or low")

inEpochs = int(input("Insert amount of epochs from at least 1 (more than 10 is not recommended): "))
if (inEpochs <= 0):
    raise ValueError("Epoch value is too low")

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale the data so that the values are from 0 - 1
x_train = x_train / 255
x_test = x_test / 255

# Flattening the train and test data
x_train_flattened = x_train.reshape(len(x_train), 28*28)
x_test_flattened = x_test.reshape(len(x_test), 28*28)

'''Part 1 - Create a simple neural network in Keras
Sequential create a stack of layers'''
model = keras.Sequential([keras.layers.Dense(10, input_shape = (784,), activation = 'sigmoid')])

# Optimizer will help in backpropagation to reach better global optima
model.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

# Does the training | 1 epoch is basically fine
model.fit(x_train_flattened, y_train, epochs = inEpochs)

# Use model from image x_test and get 10 numbers in y_example
y_example = model.predict(x_test_flattened)

# Evaluate the accuracy of test data
model.evaluate(x_test_flattened, y_test)

# Queue the image
plt.matshow(x_test[image])

# Make the predictions
y_predicted = model.predict(x_test_flattened)

for i in range(len(y_example[image])):
    print(f"Number {i}: {y_example[image][i]:.4f}")

print(f"Predicted number: {y_test[image]}")

print(f"Was the number not correct? Try using more epochs")

# Show window
plt.show()