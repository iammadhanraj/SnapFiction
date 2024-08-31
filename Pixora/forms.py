from django import forms
from .models import ImageRequest

class ImageRequestForm(forms.ModelForm):
    class Meta:
        model = ImageRequest
        fields = ['prompt']
