from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def jay(request):
    return render(request , 'fees/fees1.html')

def jay2(request):
    return render(request , 'fees/fees2.html')