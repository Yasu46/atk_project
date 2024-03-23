from django import forms
from .models import ATKResult

class ATKResultForm(forms.ModelForm):
    class Meta:
        model = ATKResult
        fields = ['result', 'image']

    def __init__(self, *args, **kwargs):
        super(ATKResultForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'w-full p-2 mt-1 border rounded-md'
