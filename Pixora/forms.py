from django import forms

class ImagePromptForm(forms.Form):
    prompt = forms.CharField(label='Image Prompt', max_length=100)
