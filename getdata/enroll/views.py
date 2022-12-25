from urllib import request
from django.shortcuts import render
from enroll.forms import SR
from django.http import HttpResponseRedirect
# Create your views here.


def tnk(request):
    return render(request , 'enroll/suc.html')

    

def showdata(request):
    if request.method =="POST":
        fm = SR(request.POST)
        if fm.is_valid():
            print('form Validation')
            name = fm.cleaned_data['name'] 
            email = fm.cleaned_data['email']
            mobile = fm.cleaned_data['mobile']
            passwd = fm.cleaned_data['passwd']
            print('name:' , name )
            print('email:' ,email )
            print('mobile:', mobile)
            print('passwd: ',passwd)
            print(fm.cleaned_data)
            #return render(request , 'enroll/suc.html' , {'nm':name})
            return HttpResponseRedirect('/enroll/succ/')
    else:
        fm = SR()
    return render(request , 'enroll/userregister.html' , {'form':fm})