from django.urls import path
from security import views
app_name = "security"

urlpatterns = [
    path('edit/', views.EditView.as_view(), name='edit'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('singup/', views.SingUpView.as_view(), name='singin'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
