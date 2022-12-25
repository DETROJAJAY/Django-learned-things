from django.shortcuts import render
from enroll.forms import SR
# Create your views here.

def showdata(request):
    fm = SR(auto_id=False , label_suffix=' ' , initial= {'name':'jay' , 'email':'@gmail.com'})
    fm.order_fields(field_order=['email','name'])
    return render(request , 'enroll/userregister.html' , {'form':fm})