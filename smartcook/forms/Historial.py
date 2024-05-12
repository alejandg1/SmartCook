from django.forms import ModelForm
from app1 import Historial


class CreditForm(ModelForm):
    class Meta:
        model = Historial
        fields = '__all__'
        exclude = []
