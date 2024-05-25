from django.forms import ModelForm
from app1 import TempImg


class CreditForm(ModelForm):
    class Meta:
        model = TempImg
        fields = '__all__'
        exclude = []
