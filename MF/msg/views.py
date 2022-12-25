from email import message
from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

def reg(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.add_message(request,messages.SUCCESS , "Your Account has been crated")
            messages.success(request ,"Your Account has been crated" )
            messages.info(request,"this is free of cost")


            print(messages.get_level(request))
            messages.debug(request,"this is dubugging...")
            messages.set_level(request , messages.DEBUG)
            messages.debug(request,"this is 2nd dubugging...")


            messages.warning(request , "this is the last warning")
            messages.error(request , "ohh somthin get error")
    else:
        fm = StudentRegistration()
    return render(request , 'msg/userregis.html' , {'form':fm})