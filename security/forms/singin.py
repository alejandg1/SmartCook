from django import forms
from django.forms import ModelForm
from security.models import User


class SinginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
