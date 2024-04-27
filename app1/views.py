from django.shortcuts import render
from .camera import capture, analysis


def index(request):
    return render(request, 'index.html')


def photo(request):
    camera = capture.camera()
    camera.takePhoto()
    # data = analysis.GetTempPhoto()
    # temp = analysis.Photo(data)
    # temp.PrintPhoto()
    analysis.getItems()
    return render(request, 'index.html')
