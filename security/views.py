from django.views.generic import TemplateView ,FormView, CreateView, UpdateView
from django.shortcuts import redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from security.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import PasswordChangeForm
from security.forms import forms


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = User.objects.get(pk=self.request.user.pk)
        return context


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cambiar contraseña'
        context['button'] = 'Cambiar'
        context['back_url'] = reverse_lazy('security:profile')
        return context


class EditView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'login.html'
    form_class = forms.EditForm
    success_url = reverse_lazy('security:profile')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = reverse_lazy('smartcook:index')
        context['title'] = 'editar usuario'
        context['button'] = 'Guardar'
        return context

class LoginView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('smartcook:index')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'inicio de sesión'
        context['button'] = 'Login'
        context['back_url'] = reverse_lazy('smartcook:index')
        return context


class LogoutView(LoginRequiredMixin, TemplateView):
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('smartcook:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SingUpView(CreateView):
    template_name = 'singup.html'
    form_class = forms.SingupForm
    success_url = reverse_lazy('smartcook:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'registro'
        context['button'] = 'Registrar'
        context['back_url'] = reverse_lazy('smartcook:index')
        return context

    def form_valid(self, form):
        self.object = form.save()
        form.instance.set_password(form.cleaned_data['password1'])
        form.instance.save()
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'])
        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            form.add_error(None, 'Error al iniciar sesión')
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('smartcook:index')
        return super().dispatch(request, *args, **kwargs)
