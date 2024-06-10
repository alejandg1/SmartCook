from django.views.generic import TemplateView, FormView
from django.http import HttpResponse
import json
import base64
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from smartcook.forms import Img
from django.contrib.auth.mixins import LoginRequiredMixin

tempURL = './temp/temp.png'

fs = FileSystemStorage()


# def saveImg(request):
#     existente = models.TempImg.objects.get(
#         userID=request.user)
#     if (existente is not None):
#         existente.image = request.FILES['image']
#         existente.save()
#     else:
#         models.TempImg.objects.create(
#             image=request.FILES['image'], userID=models.User.objects.get(pk=request.user.pk))


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
    back_url = reverse_lazy('smartcook:kitchen')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Subir imagen'
        context['button'] = 'Subir'
        context['back_url'] = self.back_url
        return context

    def post(self, request, *args, **kwargs):
        try:
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                image = form.cleaned_data['image']
                data = base64.b64encode(image.read()).decode('utf-8')
                request.session['image'] = data
                return redirect('smartcook:recognition')
        except Exception as e:
            print(e)


class RecognitionView(LoginRequiredMixin, TemplateView):
    template_name = 'recognition.html'
    back_url = reverse_lazy('smartcook:kitchen')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Resultados'
        context['back_url'] = self.back_url
        context['image'] = self.request.session['image']
        return context


def PostImage(request):
    try:
        if request.method == 'POST':
            image = json.loads(request.body)
            request.session['image'] = image
            return HttpResponse(status=200)
    except Exception as e:
        print(e)
        return HttpResponse(status=500)
