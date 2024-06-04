from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from smartcook.forms import Img
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import IA


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
    success_url = reverse_lazy('smartcook:recognition')
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
                imgData = image.read()
                IA.TEMP_IMG_DATA = imgData
        except Exception as e:
            print(e)

    def dispatch(self, request, *args, **kwargs):
        return redirect('smartcook:recognition')


class RecognitionView(LoginRequiredMixin, TemplateView):
    template_name = 'recognition.html'
    back_url = reverse_lazy('smartcook:camera')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reconocimiento de imagen'
        context['back_url'] = self.back_url
        return context


class PostImage(FormView):
    form_class = Img.ImgForm
    success_url = reverse_lazy('smartcook:recognition')
    back_url = reverse_lazy('smartcook:kitchen')

    def post(self, request, *args, **kwargs):
        try:
            form = self.form_class(request.POST, request.FILES)
            image = form.cleaned_data['image']
            imgData = image.read()
            IA.TEMP_IMG_DATA = imgData
        except Exception as e:
            print(e)

    def dispatch(self, request, *args, **kwargs):
        return redirect('smartcook:recognition')


# proceso anterior post galeria

    # try:
    #     if request.method == 'POST':
    #         existente = models.TempImg.objects.get(
    #             userID=request.user)
    #         if (existente is not None):
    #             existente.image = request.FILES['image']
    #             existente.save()
    #         else:
    #             models.TempImg.objects.create(
    #                 image=request.FILES['image'],
    #                 userID=models.User.objects.get(
    #                     pk=request.user.pk))
    #
    # except Exception as e:
    #     print(e)
    #     return HttpResponse('Image upload failed')
    # return HttpResponse('Image upload success')
