from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from security.models import User
from security.forms import edit, singin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# Create your views here.


class ProfileView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('smartcook:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = User.objects.get(pk=self.request.user.pk)
        return context


class EditView(LoginRequiredMixin, FormView):
    model = User
    template_name = 'edit.html'
    context_object_name = 'edit_user'
    success_url = reverse_lazy('security:profile')
    form_class = edit.EditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = User.objects.get(pk=self.request.user.pk)
        return context


class LoginView(LoginView):
    template_name = 'login.html'
    # context_object_name = 'login'
    # form_class = login.LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('smartcook:index')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'inicio de sesión'
        context['button'] = 'Login'
        return context


@login_required
def LogoutView(request):
    logout(request)
    return redirect('smartcook:index')


class SinginView(LoginView):
    template_name = 'singin.html'
    # context_object_name = 'singin'
    # success_url = reverse_lazy('smartcook:index')
    # form_class = singin.SinginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('smartcook:index')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro'
        context['button'] = 'Singin'
        return context
