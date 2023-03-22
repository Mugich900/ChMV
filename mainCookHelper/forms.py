from django import forms
from .models import Recepts

class ReceptForm(forms.ModelForm):
    class Meta:
        model = Recepts
        fields = {'title', 'ingredients', 'text', 'annotation',  }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'post_atribute'}),
            'text': forms.Textarea(attrs={'cols': 100, 'rows': 20, 'class': 'post_atribute'}),
            'annotation': forms.Textarea(attrs={'cols': 100, 'rows': 20,'class': 'post_atribute'}),
            'ingredients': forms.Textarea(attrs={'cols': 50, 'rows': 10, 'class': 'post_atribute'}),
        }