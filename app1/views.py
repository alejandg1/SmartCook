from django.shortcuts import render
from .camera import capture


def index(request):
    return render(request, 'index.html')


def photo(request):
    photo = capture.takePhoto()
    print(photo)
    return render(request, 'index.html')
