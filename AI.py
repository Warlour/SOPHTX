import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

len(x_train)
# 60000

len(x_test)
# 10000

# Finding the shape of individual sample
x_train[0].shape
# (28, 28)

x_train[0]

plt.matshow(x_train[0])