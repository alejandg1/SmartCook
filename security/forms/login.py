from django.forms import ModelForm
from security.models import User


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
