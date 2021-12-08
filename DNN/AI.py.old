import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

print(f"Tensorflow version: {tf.__version__}")

learn = tf.contrib.learn

tf.logging.set_verbosity(tf.logging.ERROR)

# Importing dataset using MNIST Data
mnist = learn.datasets.load_dataset('mnist')
data = mnist.train.images
labels = np.asarray(mnist.train.labels, dtype = np.int32)
test_data = mnist.test.images
test_labels = np.asarray(mnist.test.labels, dtype = np.int32)
# Outputs the retrieval of the dataset

# Making the dataset
max_examples = 10000
data = data[:max_examples]
labels = labels[:max_examples]

# Plotting dataset via matplotlib
def display(i):
    img = test_data[i]
    plt.title('label : {}'.format(test_labels[i]))
    plt.imshow(img.reshape((28, 28)))

# Display image as 28 by 28 pixels
display(0)