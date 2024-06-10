from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import numpy as np
import matplotlib.pyplot as plt

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename


    def predict(self):
        # load model
        model = load_model(os.path.join("model", "DenseNet121.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (256, 256))
        plt.imshow(plt.imread(imagename))
        test_image = image.img_to_array(test_image)
        test_image = test_image/255
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)
        result = result.ravel()
        classess = ["Fusarium Wilt", "Leaf Curl Disease", "Healthy Leaf", "Healthy Plant"]
        max = result[0]
        index = 0;
        # Loop through the array
        for i in range(0, len(result)):
            # compare elements of array with max
            if (result[i] > max):
                max = result[i];
                index = i

        # print("Largest element present in given array: " + str(max) +" And it belongs to " +str(classess[index]) +" class.");
        pred = str(classess[index])
        return pred