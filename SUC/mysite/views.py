from django.shortcuts import render

def home(re):
    print("I am Home View")
    return render(re, 'mysite/home.html')

def about(re):
    print("I amAbout View")
    return render(re, 'mysite/about.html')
