from django.shortcuts import render

# Create your views here.

def learn_django(request):
    return render(request , 'course/home.html')

def learn_dj(request):
    return render(request , 'course/about.html')