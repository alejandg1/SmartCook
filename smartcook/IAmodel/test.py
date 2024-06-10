from ultralytics import YOLO
data = '~/Descargas/ingredients detection.v1i.yolov8'
test_img = data+'/test/images/034_PNG.rf.4cb4506c78cfdcf75ca210eb4178f5ba.jpg'


class model:
    def __init__(self):
        self.model = YOLO('./yolov8l.pt')

    def export(self):
        self.model.export(format='onnx')

    def train(self):
        self.model.train(
            data='~/Descargas/ingredients detection.v1i.yolov8/data.yaml',
            epochs=2,
            batch=8,
            imgsz=640)

    def detect(self, img):
        self.model(img)


test_m = model()
test_m.detect("./test.jpg")
