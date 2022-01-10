from django import forms
from . models import DropDownList

class DropDownForm(forms.ModelForm):
    class Meta:
        model = DropDownList
        fields = '__all__'