from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    userID = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    Username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'Username'
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return self.Username

    def set_password(self, password):
        self.password = password
