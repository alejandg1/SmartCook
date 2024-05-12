from django.views.generic import TemplateView
from django.urls import reverse_lazy
from security.models import User
from security.forms import edit, login, singin

# Create your views here.


class ProfileView(TemplateView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'


class EditView(TemplateView):
    model = User
    template_name = 'edit.html'
    context_object_name = 'edit_user'
    success_url = reverse_lazy('security:profile')
    form_class = edit.EditForm


class LoginView(TemplateView):
    model = User
    template_name = 'login.html'
    context_object_name = 'login'
    success_url = reverse_lazy('smartcook:index')
    form_class = login.LoginForm


class SinginView(TemplateView):
    model = User
    template_name = 'singin.html'
    context_object_name = 'singin'
    success_url = reverse_lazy('smartcook:index')
    form_class = singin.SinginForm
