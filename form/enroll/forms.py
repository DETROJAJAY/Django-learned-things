from operator import attrgetter
from django import forms 

class SR(forms.Form):
    name = forms.CharField(label='your Name' , required=False, disabled=True,help_text="max 60 words" , 
            widget=forms.Textarea(attrs={'class':'somecss1'}))
    email = forms.EmailField(widget=forms.CheckboxInput())
    mobile = forms.IntegerField(widget=forms.PasswordInput())
    key = forms.CharField(widget=forms.HiddenInput())