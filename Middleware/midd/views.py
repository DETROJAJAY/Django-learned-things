from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse
def home(re):
    print("i am view")
    return HttpResponse("This is home page")

def exc(re):
    print("I aam Excp view")
    a = 10/0
    return HttpResponse("This is Excp view")

def tem(re):
    print("I am template view")
    context = {"name":"jay"}
    return TemplateResponse(re, 'midd/temp.html', context)