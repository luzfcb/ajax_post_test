from django import forms
from .models import Document


class Formulario(forms.ModelForm):
    header = forms.CharField(widget=forms.Textarea, label='', initial=' ')
    content = forms.CharField(widget=forms.Textarea, label='', initial=' ')
    footer = forms.CharField(widget=forms.Textarea, label='', initial=' ')

    class Meta:
        model = Document
        fields = ('header', 'content', 'footer')
