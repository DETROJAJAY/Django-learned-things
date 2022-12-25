from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def func(request):
    return HttpResponse("This is second")

def func2(request):
    return HttpResponse("<h1>helloo jay</h1>")