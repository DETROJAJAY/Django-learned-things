from operator import attrgetter
from django import forms 

class SR(forms.Form):
    name = forms.CharField(label='your Name')
    email = forms.EmailField()
    mobile = forms.IntegerField()
    passwd = forms.CharField(widget = forms.PasswordInput)