from django import forms


class ImgForm(forms.Form):
    image = forms.ImageField(label='Select an image',
                             widget=forms.FileInput(
                                 attrs={'class': 'form-control'}))
