from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class HistoryView(TemplateView):
    template_name = 'history.html'


class KitchenView(TemplateView):
    template_name = 'kitchen.html'


class SearchView(TemplateView):
    template_name = 'search.html'


class RecipeView(TemplateView):
    template_name = 'components/recipe.html'


class CameraView(TemplateView):
    template_name = 'camera.html'


class GaleryView(TemplateView):
    template_name = 'galery.html'
