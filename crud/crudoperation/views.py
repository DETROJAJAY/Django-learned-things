import imp
from multiprocessing import context
from django.shortcuts import HttpResponseRedirect, redirect, render
from crudoperation.models import Employee
from django.core.mail import send_mail
from sms import send_sms
from django.conf import settings
from django.db.models import Max
# Create your views here.
def open(request):
    emp  = Employee.objects.all()

    context={
        'emp':emp,
    }
    return render(request,'crudoperation/index.html',context)


def add(request):
    regno = 1001 if Employee.objects.count() == 0 else Employee.objects.aggregate(max=Max('userid'))["max"] + 1
    if request.method =='POST':
        name =request.POST.get('name')
        email =request.POST.get('email')
        address =request.POST.get('address')
        phone =request.POST.get('phone')

        emp = Employee(
            userid = regno,
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        emp.save()
        to = emp.email
        message = 'hey' +emp.name+',you are now successfully register with us.'
        send_mail(
        'Thank you for Registration',
        message,
        'dairyfarmmgtsys@gmail.com',
        [to],
        fail_silently=False,
        )
        
        #ppt= emp.phone
        send_sms(
            message,
            'dairyfarmmgtsys@gmail.com',
            ['+919104063351'],
            fail_silently=False
        )
        return redirect('my/')
           
    return render(request,'crudoperation/index.html',context)


def edit(request):
    emp  = Employee.objects.all()
    context={
        'emp':emp,
    }   
    return render(request,'crudoperation/index.html',context)

def update(request,id):
    if request.method == 'POST':
        name =request.POST.get('name')
        email =request.POST.get('email')
        address =request.POST.get('address')
        phone =request.POST.get('phone')


        emp = Employee(
            id=id,
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        emp.save()
        return HttpResponseRedirect('/')
    return render(request,'crudoperation/index.html')

def delete(request,id):
    emp  = Employee.objects.filter(id = id)
    emp.delete()
    context={
        'emp':emp,
    }
    
    return HttpResponseRedirect('/')
