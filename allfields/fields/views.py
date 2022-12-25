from django.shortcuts import render
from .forms import AF
from django.http import HttpResponseRedirect

# Create your views here.
def AD(request):
     return render(request , 'fields/done.html')

def all_fields(request):
    if request.method == "POST":
        cf = AF(request.POST)
        if cf.is_valid():
            print('name: ' , cf.cleaned_data['name'])
            print('agree: ',cf.cleaned_data['agree'])
            print('number: ' , cf.cleaned_data['number'])
            print('price: ' , cf.cleaned_data['price'])
            print('rate: ' , cf.cleaned_data['rate'])
            print('feedback: ' , cf.cleaned_data['feedback'])
            print('pass : ' , cf.cleaned_data['password'])
            return HttpResponseRedirect('/show/done/')
    else:
        cf = AF()
    return render(request , 'fields/form_field.html' , {'vari': cf})