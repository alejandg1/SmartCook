from django.forms import ModelForm
from smartcook.models import TempImg


class ImgForm(ModelForm):
    class Meta:
        model = TempImg
        fields = ['image']
        exclude = ['userID']
