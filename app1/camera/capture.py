import cv2
import imutils
ImgPath = 'temp.jpg'

def takePhoto():
    camara = cv2.VideoCapture(0)
    while True :
        ret, frames = camara.read()
        if ret == False: break
        frame =  imutils.resize(frames, width=640)
        cv2.imshow('camera',frame)
        k =  cv2.waitKey(1)
        if k == ord('q'):
            cv2.imwrite(ImgPath, frame)
            break
    camara.release()
    cv2.destroyAllWindows()
