from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    UserManager,
    PermissionsMixin)

# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    userID = models.AutoField(primary_key=True)
    last_name = models.CharField('last name',
                                 max_length=20,
                                 blank=True)
    first_name = models.CharField('first name',
                                  max_length=20,
                                  blank=True)
    email = models.EmailField('email',
                              unique=True,
                              blank=False,
                              null=False)
    username = models.CharField('username',
                                max_length=20,
                                unique=True,
                                blank=False)
    is_staff = models.BooleanField('staff status',
                                   default=False)
    is_active = models.BooleanField('active',
                                    default=True)
    is_superuser = models.BooleanField('superuser',
                                       default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    FIRST_NAME_FIELD = 'first_name'
    LAST_NAME_FIELD = 'last_name'
    PASSWORD_FIELD = 'password'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username
