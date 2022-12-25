from optparse import Values
from django.shortcuts import render,HttpResponseRedirect
from .models import User
from .forms import StudentRegistration, Teacher



#This function is for Show and add item to databse
def Add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            ph = fm.cleaned_data['phone']
            em = fm.cleaned_data['email']
            pd = fm.cleaned_data['password']
            reg = User(name=nm,phone = ph,email=em,password=pd)
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stud = User.objects.all()

    return render(request , 'enroll/add&show.html' , {'form':fm , 'stu':stud})



#This function is for deelete item from database
def Delete_data(request , id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')



#This function is for update or edit data in databse
def Update_data(request,id):
    if request.method == "POST":

        for i in User.objects.filter(pk=id).values('password'):
            oldpass = i.get('password')

        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST , instance=pi)
        if fm.is_valid():
            if oldpass == fm.cleaned_data['password']:
                fm.save()
                return HttpResponseRedirect('/')
            else:
                return render(request,'enroll/updatestudent.html',{'wow':fm})
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        
    return render(request,'enroll/updatestudent.html',{'form':fm})


#for new tacher form
def Teacher_daata(request):
    if request.method=='POST':
        ext = Teacher(request.POST)
        if ext.is_valid():
            ext.save()
    else:
        ext = Teacher()
    return render(request, 'enroll/Teacher.html' , {'form':ext})