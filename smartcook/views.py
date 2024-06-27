from django.views.generic import TemplateView, FormView
from security.models import User
from smartcook.models import Historial, DetHistorial
import base64
from django.http import HttpResponse
from . import functions
import json
from django.shortcuts import redirect
from django.urls import reverse_lazy
from smartcook.forms import Img
from django.contrib.auth.mixins import LoginRequiredMixin


imgPath = functions.directory


class IndexView(TemplateView):
    template_name = 'index.html'


class HistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'history.html'

    def get_context_data(self, **kwargs):
        fixed = []
        context = super().get_context_data(**kwargs)
        hist = Historial.objects.get(user=self.request.user)
        recetas = DetHistorial.objects.filter(histID=hist.histID)
        for rec in recetas:
            nombre = rec.Recipe
            ingredientes = rec.Ingredients.split(',')
            pasos = rec.Instructions.split(',')
            receta = {
                'nombre': nombre,
                'ingredientes': ingredientes,
                'pasos': pasos
            }
            print(receta)
            fixed.append(receta)

        if fixed == []:
            context['recetas'] = [{'nombre': 'sin recetas disponibles'}]
            return context
        context['recetas'] = fixed
        return context


class KitchenView(LoginRequiredMixin, FormView):
    template_name = 'kitchen.html'
    form_class = Img.ImgForm
    back_url = reverse_lazy('smartcook:index')

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
                functions.saveImg(data)
                functions.compress()
                return redirect('smartcook:recognition')
        except Exception as e:
            print(e)


class SearchView(LoginRequiredMixin, TemplateView):
    template_name = 'search.html'


class RecipeView(LoginRequiredMixin, TemplateView):
    template_name = 'components/recipe.html'


class CameraView(LoginRequiredMixin, TemplateView):
    template_name = 'camera.html'


class RecognitionView(LoginRequiredMixin, TemplateView):
    template_name = 'recognition.html'
    back_url = reverse_lazy('smartcook:kitchen')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Resultados'
        context['back_url'] = self.back_url
        with open(imgPath+'image.jpg', 'rb') as f:
            img = base64.b64encode(f.read()).decode('utf-8')
        context['img'] = img

        recipes = []
        resp = functions.GPT()
        with open(imgPath+'response.json', 'w') as f:
            json.dump(resp, f)
        with open('smartcook/../response.json', 'r') as f:
            resp = json.load(f)
        resp = functions.parse_resp(resp)
        with open('smartcook/parsed.json', 'w') as f:
            json.dump(resp, f)
        for i in resp['recipes']:
            rec = functions.Recipe(
                i['nombre'], i['pasos'])
            for j in i['ingredientes']:
                rec.add_ingredient(j)
            recipes.append(rec)
        context['recetas'] = recipes
        context['ingredientes'] = resp['ingredients']
        return context


def PostImage(request):
    try:
        if request.method == 'POST':
            image = json.loads(request.body)
            functions.saveImg(image['image'])
            functions.compress()
            request.session['image'] = image['image']
            return HttpResponse(status=200)
    except Exception as e:
        print(e)
        return HttpResponse(status=500)
