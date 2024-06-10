from django.urls import path
from smartcook import views
app_name = "smartcook"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('kitchen/', views.KitchenView.as_view(), name='kitchen'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('history/', views.HistoryView.as_view(), name='history'),
    path('recipe/', views.RecipeView.as_view(), name='recipe'),
    path('camera/', views.CameraView.as_view(), name='camera'),
    path('galery', views.GaleryView.as_view(), name='galery'),
    path('recognition/', views.RecognitionView.as_view(), name='recognition'),
    path('img/', views.PostImage, name='image'),
]
