from django.shortcuts import render,HttpResponse
from blog import signals

# Create your views here.

def home(request):
    # a = 10/0
    signals.notification.send(sender = None , request=request ,user=['jay','dj']) #aapdu banavelu signal ne page ma send krva mate
    return HttpResponse("this is home page")