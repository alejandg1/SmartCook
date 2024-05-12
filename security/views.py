from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from security.models import User
from security.forms import edit, login, singin

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


class LoginView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'login.html'
    context_object_name = 'login'
    success_url = reverse_lazy('smartcook:index')
    form_class = login.LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login'] = User.objects.get(pk=self.request.user.pk)
        return context


class SinginView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'singin.html'
    context_object_name = 'singin'
    success_url = reverse_lazy('smartcook:index')
    form_class = singin.SinginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['singin'] = User.objects.get(pk=self.request.user.pk)
        return context
