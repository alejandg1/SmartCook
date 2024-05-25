from django.forms import ModelForm
from app1 import DetHistorial


class CreditForm(ModelForm):
    class Meta:
        model = DetHistorial
        fields = '__all__'
        exclude = []
