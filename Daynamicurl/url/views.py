from django.shortcuts import render

# Create your views here.

def home(request , check):
    print(check)
    return render(request , 'url/home.html' , {'ch':check})

def show_data(request,my_id):
    if my_id==1:
        student = {'id':my_id , 'name':'jay'}
    if my_id==2:
        student = {'id':my_id , 'name':'heet'}
    if my_id==3:
        student = {'id':my_id , 'name':'meet'}
    return render(request , 'url/data.html' , student)

def show_subdata(request,my_id,my_subid):
    if my_id=='spectrom' and my_subid == 6:
        student = {'id':my_id , 'name':'jay' , 'info' : 'sub Details'}
    if my_id==2 and my_subid == 7:
        student = {'id':my_id , 'name':'heet' ,'info' : 'sub Details'}
    if my_id==3 and my_subid == 8:
        student = {'id':my_id , 'name':'meet' ,'info' : 'sub Details'}
    return render(request , 'url/data.html' , student)
