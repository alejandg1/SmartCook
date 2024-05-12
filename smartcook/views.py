from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class HistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'history.html'


class KitchenView(LoginRequiredMixin, TemplateView):
    template_name = 'kitchen.html'


class SearchView(LoginRequiredMixin, TemplateView):
    template_name = 'search.html'


class RecipeView(LoginRequiredMixin, TemplateView):
    template_name = 'components/recipe.html'


class CameraView(LoginRequiredMixin, TemplateView):
    template_name = 'camera.html'


class GaleryView(LoginRequiredMixin, TemplateView):
    template_name = 'galery.html'
