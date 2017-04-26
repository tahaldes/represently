from django import forms

from .models import Zipcode


class ZipcodeForm(forms.ModelForm):
    class Meta:
        model = Zipcode
        fields = ['zip']
