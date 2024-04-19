from django.shortcuts import render
from .camera import capture, analysis


def index(request):
    return render(request, 'index.html')


def photo(request):
    capture.takePhoto()
    data = analysis.GetTempPhoto()
    temp = analysis.Photo(data)
    temp.PrintPhoto()
    return render(request, 'index.html')
