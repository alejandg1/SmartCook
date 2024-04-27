# import tensorflow as tf
import cv2
import numpy as np
# import keras
from app1 import constanst 
# from keras.applications.resnet50 import preprocess_input, decode_predictions, ResNet50

# def GetTempPhoto():
#     img = cv2.imread(constanst.TempImgPath)
#     return img

# # class Photo:
# #     def __init__(self, img):
# #         self.data = img

# #     def PrintPhoto(self):
# #         print(self.data)

# #     def getItems(self):
# #         model = ResNet50(weights='imagenet')
# #         img= keras.utils.load_img(constanst.TempImgPath, target_size=(224, 224))
# #         array = keras.utils.array_to_img(img)
# #         array = np.expand_dims(array, axis=0)
# #         array = preprocess_input(array)
# #         prediction = model.predict(array)
# #         print('Predicted:', decode_predictions(prediction, top=3)[0])

# #     def getKeyWords(self):
# #         pass


# def getItems():
#     #model = ResNet50(weights='imagenet')
#     model = tf.keras.applications.InceptionV3(weights='imagenet')
#     img= keras.utils.load_img(constanst.TestImgPath, target_size=(299, 299))
#     array = keras.utils.array_to_img(img)
#     array = np.expand_dims(array, axis=0)
#     array = preprocess_input(array)
#     prediction = model.predict(array)
#     print('Predicted:', decode_predictions(prediction, top=4)[0])