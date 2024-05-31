from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from security.models import User
from django.contrib.auth.forms import UserChangeForm


class EditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email']
        exclude = ['password']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
        }


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña'
        }
        
