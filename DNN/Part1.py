# See https://dev.to/milindsoorya/mnist-handwritten-digit-classification-using-tensorflow-3k7d

import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# len(x_train)
# Output: 60000

# len(x_test)
# Output: 10000

# Finding the shape of individual sample
# x_train[0].shape
# Output: (28, 28)
# Each sample is a 28x28 pixel image

# Show following sample
# plt.matshow(x_train[0])

# y_train[0]
# Output: 5

# Show first 5 data
# y_train[:5]
# Output: array([5, 0, 4, 1, 9], dtype=uint8)

# x_train.shape
# Output: (60000, 28, 28)

# Scale the data so that the values are from 0 - 1
x_train = x_train / 255
x_test = x_test / 255

# x_train[0]

# Flattening the train and test data
x_train_flattened = x_train.reshape(len(x_train), 28*28)
x_test_flattened = x_test.reshape(len(x_test), 28*28)

# x_train_flattened.shape
# Output: (60000, 784)

'''Part 1 - Create a simple neural network in Keras
Sequential create a stack of layers'''
model = keras.Sequential([keras.layers.Dense(10, input_shape = (784,), activation = 'sigmoid')])

# Optimizer will help in backpropagation to reach better global optima
model.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

# Does the training
model.fit(x_train_flattened, y_train, epochs = 5)

# Evaluate the accuracy of test data
model.evaluate(x_test_flattened, y_test)

# Show the image
plt.matshow(x_test[0])

# Show window
plt.show()

# Make the predictions
y_predicted = model.predict(x_test_flattened)

# Find the maximum value using numpy
# np.argmax(y_predicted[0])
# Output: 7

# Converting y_predicted from whole numbers to integers
# So that we can use it in confusion matrix
# In short we are argmaxing the entire prediction
y_predicted_labels = [np.argmax(i) for i in y_predicted]

# print(y_predicted_labels[:5])
# Output: [7, 2, 1, 0, 4]

cm = tf.math.confusion_matrix(labels = y_test, predictions = y_predicted_labels)
# print(cm)
'''
Output: 
tf.Tensor(
[[ 961    0    1    2    0    5    8    2    1    0]
 [   0 1117    3    2    0    1    4    2    6    0]
 [   6   10  926   17    7    1   13   10   37    5]
 [   2    1   20  938    1   12    2    9   16    9]
 [   1    2    5    2  905    0   16    4    9   38]
 [  10    3    3   51    9  753   23    6   27    7]
 [   7    3    5    1    7    7  925    2    1    0]
 [   1    7   24    8    8    1    0  942    1   36]
 [   8   12    7   35    9   28   10   13  840   12]
 [  11    7    1   13   28    4    0   17    4  924]], shape=(10, 10), dtype=int32)
'''

# We use seaborn module to make the confusion matrix 'look good'
import seaborn as sn
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')

plt.show()

print(y_predicted[1])