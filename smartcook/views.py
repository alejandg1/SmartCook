from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
import json
from smartcook.forms import Img
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from django.views.decorators.csrf import csrf_exempt


def saveImg(request):
    existente = models.TempImg.objects.get(
        userID=request.user)
    if (existente is not None):
        existente.image = request.FILES['image']
        existente.save()
    else:
        models.TempImg.objects.create(
            image=request.FILES['image'],
            userID=models.User.objects.get(
                pk=request.user.pk))


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


class GaleryView(LoginRequiredMixin, FormView):
    template_name = 'forms.html'
    form_class = Img.ImgForm
    success_url = reverse_lazy('smartcook:kitchen')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Subir imagen'
        context['button'] = 'Subir'
        context['back_url'] = reverse_lazy('smartcook:kitchen')
        return context

    def post(self, request, *args, **kwargs):
        try:
            if request.method == 'POST':
                existente = models.TempImg.objects.get(
                    userID=request.user)
                if (existente is not None):
                    existente.image = request.FILES['image']
                    existente.save()
                else:
                    models.TempImg.objects.create(
                        image=request.FILES['image'],
                        userID=models.User.objects.get(
                            pk=request.user.pk))

        except Exception as e:
            print(e)
            return HttpResponse('Image upload failed')
        return HttpResponse('Image upload success')


@ csrf_exempt
def PostImage(request):
    req = json.loads(request.body)
    try:
        existente = models.TempImg.objects.get(
            userID=models.User.objects.get(
                pk=req['userID']))
        if (existente is not None):
            existente.image = req['image']
            existente.save()
        else:
            models.TempImg.objects.create(
                image=req['image'],
                userID=models.User.objects.get(
                    pk=req['userID']))
    except Exception as e:
        print(e)
        return HttpResponse('Image upload failed')
    return HttpResponse('Image upload success')
