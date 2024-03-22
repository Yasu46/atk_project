from django import forms
from .models import ATKResult

class ATKResultForm(forms.ModelForm):
    class Meta:
        model = ATKResult
        fields = ['result', 'image']
