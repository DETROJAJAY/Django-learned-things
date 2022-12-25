from django import forms
from .models import user

class studentdata(forms.ModelForm):
    # name = forms.CharField(max_length=15)
    class Meta:
        model = user
        fields = ['name','password','email']
        error_messages =  {
            'name' : {'required':'Naam likhna pdta hai'},
            'password' : {'required':'pass to dalo'}
            }
        labels = {'name':'Enter name ','password':'Enter pass','email':'Enter email'}
        help_texts = {'name' : 'Enter your name'}
        widgets = {
            'password':forms.PasswordInput,
            'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Write here'})
        }