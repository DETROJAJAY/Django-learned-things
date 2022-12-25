from django.shortcuts import render
from enroll.models import student
# Create your views here.

def stu_info(request):
    stud = student.objects.all()
    #stud = student.objects.get(pk = 1)
    return render(request , 'enroll/sd.html' , {'stu':stud})