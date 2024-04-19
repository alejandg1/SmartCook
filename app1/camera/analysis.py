# import tensorflow as tf
import cv2
from .capture import ImgPath

def GetTempPhoto():
    img = cv2.imread(ImgPath)
    return img

class Photo:
    def __init__(self, img):
        self.data = img

    def PrintPhoto(self):
        print(self.data)

    def getItems(self):
        pass

    def getKeyWords(self):
        pass
