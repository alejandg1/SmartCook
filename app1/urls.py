from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cocina/', views.cocina, name='cocina'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('historial/', views.historial, name='historial'),
    path('login/', views.login, name='login'),
    path('singin/', views.singin, name='singin'),
    path('receta/', views.receta, name='receta'),
    path('perfil/', views.perfil, name='perfil'),

    path('photo', views.photo, name='photo'),
]
