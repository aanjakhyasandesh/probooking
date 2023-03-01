from django import forms

from .models import snippet

class Auth(forms.ModelForm):
    class Meta:
        model= snippet
        fields=("username","password")