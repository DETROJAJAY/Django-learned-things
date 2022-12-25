from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(reuest):
    return HttpResponse('home page')
    
def jay(request):
    return HttpResponse('hello Dj')

def func(request):
    a = 10 + 10
    return HttpResponse(a)