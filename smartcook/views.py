from django.views.generic import TemplateView, FormView
from django.shortcuts import render
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
        # resp = functions.GPT()
        resp = {
            "recipes": [
                {
                    "name": "Pollo con papas",
                    "ingredients": ["pollo", "papas", "sal", "pimienta"],
                    "description": "Delicioso pollo con papas"
                },
            ],
            "ingredients": ["pollo", "papas", "sal", "pimienta"]

        }
        recipes = []
        for i in range(len(resp['recipes'])):
            rec = functions.Recipe(
                resp['recipes'][i]['name'], resp['recipes'][i]['description'])
            for j in range(len(resp['recipes'][i]['ingredients'])):
                rec.add_ingredient(resp['recipes'][i]['ingredients'][j])
            recipes.append(rec)
        context['recetas'] = recipes
        context['inredientes'] = resp['ingredients']
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

        # def Modal(request):
        #     name = request.GET.get('name')
        #     description = request.GET.get('desc')
        #     context = {
        #         'name': name,
        #         'desc': description
        #     }
        # return render(request, 'components/recipe.html', context)
