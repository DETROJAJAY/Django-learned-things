from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def jay(request):
    course_name = {'cname' : 'java' , 'duration' : '3 months' , 'sests' : '9'}
    return render(request , 'course/course1.html' , course_name)

def jay2(request):
    return render(request , 'course/course2.html')

def jay3(request):
    return render(request , 'home.html')