import cv2


def takePhoto():
    camara = cv2.VideoCapture(0)
    ret, imagen = camara.read()
    # cv2.imwrite('~/Imágenes/temp_photo.jpg', imagen)
    # camara.release()
    if ret:
        return imagen
    else:
        return None
