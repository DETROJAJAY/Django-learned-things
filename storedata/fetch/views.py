from django.shortcuts import render
from django.http import HttpResponseRedirect
from fetch.forms import studentdata
from .models import user

# Create your views here.
def AD(request):
    vari = studentdata(request)
    return render(request , 'fetch/done.html')


def sd(request):
    if request.method == 'POST':
        vari = studentdata(request.POST)
        if vari.is_valid():
            nm = vari.cleaned_data['name']
            em = vari.cleaned_data['email']
            ps = vari.cleaned_data['password']
            reg = user(name=nm,email=em,password=ps)
            reg.save()
            # reg = user(id=3)
            # reg.delete()
            return HttpResponseRedirect('/get/done/')
    else:
        vari = studentdata()
    return render(request , 'fetch/show.html' , {'got' : vari})
