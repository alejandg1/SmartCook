from django.shortcuts import render
from .camera import capture, analysis


def index(request):
    return render(request, 'index.html')


def historial(request):
    return render(request, 'historial.html')


def cocina(request):
    return render(request, 'cocina.html')


def login(request):
    return render(request, 'login.html')


def singin(request):
    return render(request, 'singin.html')


def busqueda(request):
    return render(request, 'busqueda.html')


def receta(request):
    return render(request, 'components/recetamodal.html')


def edit_user(request):
    return render(request, 'edit_user.html')


def perfil(request):
    return render(request, 'perfil.html')


def photo(request):
    camera = capture.camera()
    camera.takePhoto()
    # data = analysis.GetTempPhoto()
    # temp = analysis.Photo(data)
    # temp.PrintPhoto()
    analysis.getItems()
    return render(request, 'index.html')
