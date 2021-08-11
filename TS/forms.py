from .models import misdata
from django import forms


class misdataForms(forms.ModelForm):
    # date = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = misdata
        fields = '__all__'