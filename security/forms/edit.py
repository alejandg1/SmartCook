from security.models import User
from django.contrib.auth.forms import UserChangeForm


class EditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password')
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password'
        }
