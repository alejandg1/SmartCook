from django.views.generic import TemplateView
import json
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from django.views.decorators.csrf import csrf_exempt


class IndexView(TemplateView):
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


@csrf_exempt
def PostImage(request):
    req = json.loads(request)
    if req.method == 'POST':
        print(req.body)
        models.TempImg.objects.create(
            image=req.body['image'], user=req.body['user'])
        return HttpResponse('Image upload success')
    return HttpResponse('Image upload failed')
