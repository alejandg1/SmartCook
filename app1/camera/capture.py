import cv2
import imutils
from app1 import constanst

class camera:
    def __init__(self):
        self.path = constanst.TempImgPath
    def takePhoto(self):
        camara = cv2.VideoCapture(0)
        while True :
            ret, frames = camara.read()
            if ret == False: break
            frame =  imutils.resize(frames, width=640)
            cv2.imshow('camera',frame)
            k =  cv2.waitKey(1)
            if k == ord('q'):
                cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(self.path, frame)
                break
        camara.release()
        cv2.destroyAllWindows()