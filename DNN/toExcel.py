import os
import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import seaborn as sn
import xlsxwriter as xw
import time

'''
Steder markeret med * er citeret af milindsoorya fra https://dev.to/milindsoorya/mnist-handwritten-digit-classification-using-tensorflow-3k7d,
citeringen stopper ved linjeskift
'''

a = int(input("Hvor mange samples vil du gå gennem? Dette starter fra nul af: "))
b = int(input("Hvor mange epochs?: "))

start = time.time()

aiFolder = "AI Guessing"
if (not os.path.exists(aiFolder)):
    os.makedirs(aiFolder)

# *
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# * Scale the data so that the values are from 0 - 1
x_train = x_train / 255
x_test = x_test / 255

# * Flattening the train and test data
x_train_flattened = x_train.reshape(len(x_train), 28*28)
x_test_flattened = x_test.reshape(len(x_test), 28*28)

'''* Part 1 - Create a simple neural network in Keras
Sequential create a stack of layers'''
model = keras.Sequential([keras.layers.Dense(10, input_shape = (784,), activation = 'sigmoid')])

# * Optimizer will help in backpropagation to reach better global optima
model.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

def generate(repeat: int, inEpochs: int, file: str):
    '''Parameters: How many numbers to go over, how many epochs, file name to write to'''
    if (repeat <= 0):
        raise ValueError("Must repeat at least 1 time")
    if (inEpochs <= 0):
        raise ValueError("Must have at least 1 epoch")

    picFolder = f"{aiFolder}/{file}/images"
    if (not os.path.exists(picFolder)):
        os.makedirs(picFolder)

    confusionFolder = f"{aiFolder}/{file}/Confusion Matrix"
    if (not os.path.exists(confusionFolder)):
        os.makedirs(confusionFolder)

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Create new workbook/xlsx-file
    workbook = xw.Workbook(f"{aiFolder}/{file}/{file}.xlsx")

    # Add new worksheet in workbook
    worksheet = workbook.add_worksheet()

    worksheet.freeze_panes(1, 0)

    for image in range(repeat):
        repeatStart = time.time()

        # * Does the training | 1 epoch is basically fine
        model.fit(x_train_flattened, y_train, epochs = inEpochs)

        # * Use model from image x_test and get 10 numbers in y_example
        y_example = model.predict(x_test_flattened)

        # * Evaluate the accuracy of test data
        model.evaluate(x_test_flattened, y_test)

        # * Make the predictions
        y_predicted = model.predict(x_test_flattened)

        # Confusion matrix
        # * Converting y_predicted from whole numbers to integers
        y_predicted_labels = [np.argmax(i) for i in y_predicted]
        cm = tf.math.confusion_matrix(labels = y_test, predictions = y_predicted_labels)

        plt.figure(figsize = (10,7))
        sn.heatmap(cm, annot=True, fmt='d')
        plt.xlabel('Predicted')
        plt.ylabel('Truth')

        cPicName = f"Nr. {image}, Guess {y_test[image]}, Epoch {inEpochs}"

        # Save Confusion matrix as image
        plt.savefig(f"{confusionFolder}/{cPicName}.png", bbox_inches = 'tight')

        # Queue the image
        plt.matshow(x_test[image])

        picName = f"Nr. {image}, Guess {y_test[image]}"

        # Save image number (from 0 to 9999), guess, and picture to file
        plt.savefig(f"{picFolder}/{picName}.png", bbox_inches = 'tight')

        # Write to worksheet
        # write() takes the arguments of a cell and the value
        # Image numbers
        worksheet.write('A1', 'Nr.')
        worksheet.write(f'A{image+2}', image)

        # Epochs
        worksheet.write('B1', 'Epochs')
        worksheet.write(f'B{image+2}', inEpochs)

        # Predicted number
        predicted_format = workbook.add_format()
        predicted_format.set_bg_color('#33BB55')
        predicted_format.set_align('center')
        predicted_format.set_align('vcenter')
        worksheet.set_column('C:C', 16)
        worksheet.write('C1', 'Predicted number', predicted_format)
        worksheet.write(f'C{image+2}', y_test[image], predicted_format)

        # Confidence
        worksheet.set_column('D:M', 12)
        confidence_format = workbook.add_format()
        confidence_format.set_bg_color('#C4BDB7')
        confidence_format.set_align('center')
        confidence_format.set_align('vcenter')

        bestValue = 0
        for x in y_example[image]:
            if (x > bestValue):
                bestValue = x

        # For every confidence number in list: y_example[image]
        for i in range(len(y_example[image])):
            worksheet.write(f'{alphabet[i+3]}1', f'Conf. Num. {i}', confidence_format)
            # If it is not the predicted value
            if (y_example[image][i] != bestValue):
                worksheet.write(f'{alphabet[i+3]}{image+2}', f'{y_example[image][i]:.5f}', confidence_format)
            else:
                worksheet.write(f'{alphabet[i+3]}{image+2}', f'{y_example[image][i]:.5f}', predicted_format)

        '''
        Insert number image
        Thanks to patrickjlong1 | Citeringen markeret med %
        https://stackoverflow.com/questions/50945999/resize-excel-cell-to-fit-an-image
        '''
        # %
        with Image.open(f"{picFolder}/{picName}.png") as imgI:
            width_100 = imgI.width
            height_100 = imgI.height
        
        width_30 = int(round(width_100 * 0.3, 0))
        imgI = Image.open(f"{picFolder}/{picName}.png")
        wpercent = (width_30/float(width_100))
        hsize = int((float(height_100)*float(wpercent)))
        imgI = imgI.resize((width_30, hsize), Image.ANTIALIAS)
        imgI.save(f"{picFolder}/{picName}_30perc.png")
        worksheet.set_column('N:N', 18)
        
        worksheet.insert_image(f'N{image+2}', f"{picFolder}/{picName}_30perc.png")

        # % Insert confusion matrix image
        with Image.open(f"{confusionFolder}/{cPicName}.png") as imgC:
            width_100 = imgC.width
            height_100 = imgC.height
        
        width_30 = int(round(width_100 * 0.3, 0))
        imgC = Image.open(f"{confusionFolder}/{cPicName}.png")
        wpercent = (width_30/float(width_100))
        hsize = int((float(height_100)*float(wpercent)))
        imgC = imgC.resize((width_30, hsize), Image.ANTIALIAS)
        imgC.save(f"{confusionFolder}/{cPicName}_30perc.png")
        worksheet.set_column('O:O', 18)

        worksheet.insert_image(f'O{image+2}', f"{confusionFolder}/{cPicName}_30perc.png")
        worksheet.set_row(image+1, 141)
    
        plt.close('all')
        repeatEnd = time.time()
        tookTime = repeatEnd - repeatStart

        eta = tookTime*(repeat - image)
        m, s = divmod(eta, 60)
        h, m = divmod(m, 60)


        print(f"Completed {image+1} out of {repeat}", end = " | ")
        print(f"took {tookTime:.2f} seconds", end = " | ")
        if (image+1 != repeat):
            print(f"ETA: {h:.0f}h:{m:.0f}m:{s:.0f}s ({eta:.2f} seconds)", end = "\n\n")

    workbook.close()
    end = time.time()
    tookTime = end - start
    m, s = divmod(tookTime, 60)
    h, m = divmod(m, 60)
    print(f"Process took {h:.0f}h:{m:.0f}m:{s:.0f}s ({tookTime:.2f} seconds)")

    print(f"Check your 'AI Guessing' folder")

generate(a, b, "test")