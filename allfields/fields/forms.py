from cProfile import label
import string
from django import forms 
from django.core import validators


def custom(value):
    if any([k not in string.ascii_letters for k in value]):
        raise forms.ValidationError('name must be in letter ')


class AF(forms.Form):
    # error_css_class='error'
    # required_css_class='required'
    name = forms.CharField(validators=[custom],error_messages = {'required':'Enter your name'})
    email = forms.EmailField(error_messages={"required":"Enter email"})
    agree = forms.BooleanField(label='I agree' , label_suffix= '')
    number = forms.IntegerField(validators=[validators.MaxValueValidator(10000)])
    price = forms.DecimalField(min_value=10 , max_value=10000 , max_digits= 4 , decimal_places=1)
    rate = forms.FloatField()
    feedback = forms.CharField(widget=forms.TextInput(attrs={'class' : 'somecss1 comecss2' , 'id' : 'uniqueid'}))
    password = forms.IntegerField(widget=forms.PasswordInput,error_messages={'required':'wrong pass'})
    password2 = forms.IntegerField(label= 'again pass',widget=forms.PasswordInput)

    # def clean(self):
    #     clean_data =  super().clean()
    #     valname = self.cleaned_data['name']
    #     valnumber = self.cleaned_data['number']
    #     if len(valname) < 3:
    #         raise forms.ValidationError('name must be greater then 3 ')
    #     if len(str(valnumber)) != 10:
    #         raise forms.ValidationError("number must be 10 element")
        
  
    def clean(self):
        cleaned_data = super().clean()
        p1 = self.cleaned_data['password']
        p2 = self.cleaned_data['password2']
        if p1 != p2:
            raise forms.ValidationError('pass does not mach')