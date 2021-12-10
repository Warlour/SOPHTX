import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sn

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

# Make the predictions
y_predicted = model.predict(x_test_flattened)

# Confusion matrix
# Converting y_predicted from whole numbers to integers
y_predicted_labels = [np.argmax(i) for i in y_predicted]

cm = tf.math.confusion_matrix(labels = y_test, predictions = y_predicted_labels)

plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')

picFolder = "AI Guessing/Confusion Matrix"
picName = f"Nr. {image}, Guess {y_test[image]}, Epoch {inEpochs}"

# Save Confusion matrix as image
plt.savefig(f"{picFolder}/{picName}.png", bbox_inches = 'tight')

for i in range(len(y_example[image])):
    print(f"Number {i}: {(y_example[image][i]*100):.2f}%")

print(f"Predicted number: {y_test[image]}")

print(f"Was the number not correct? Try using more epochs")

# Queue the image
plt.matshow(x_test[image])

# Save image number (from 0 to 9999), guess, and picture to file
picFolder = "AI Guessing"
picName = f"Nr. {image}, Guess {y_test[image]}"

plt.savefig(f"{picFolder}/{picName}.png", bbox_inches = 'tight')