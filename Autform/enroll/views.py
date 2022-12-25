from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm, editadminprofil, edituserprofil
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate , login , logout , update_session_auth_hash
from django.contrib.auth.models import User,Group



def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request , 'Account created succesfully')
            ur = fm.save()
            group = Group.objects.get(name='admin')
            ur.groups.add(group)
    else:
        fm = SignUpForm()
    return render(request , 'enroll/signup.html' , {'form':fm})

def login_data(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')
    else:
        if request.method == "POST":
            fm = AuthenticationForm(request=request , data = request.POST)
            if fm.is_valid():
                un = fm.cleaned_data['username']
                up = fm.cleaned_data['password']
                user = authenticate(username=un , password=up)
                if user is not None:
                    login(request,user)
                    messages.success(request , 'Logged in succesfully')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        
        return render(request , 'enroll/login.html' , {'form': fm})

def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser:
                fm = editadminprofil(request.POST , instance=request.user)
                ur = User.objects.all()
            else:
                fm=edituserprofil(request.POST , instance=request.user)
                ur=None
            if fm.is_valid():
                messages.success(request , "Profile Updated")
                fm.save()
        else:
            if request.user.is_superuser:
                fm = editadminprofil(instance = request.user)
                ur = User.objects.all()
            else:
                fm = edituserprofil(instance=request.user)
                ur = None
        return render(request , 'enroll/profil.html' , {'name':request.user.username , 'form':fm , 'user':ur}) 
    else:
        messages.error(request , "First enter your login details")
        return HttpResponseRedirect('/login/')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#change password with old user
def changepass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user , data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request , fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user = request.user)
            return render(request , 'enroll/change.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/login/')

#change password without old password
def changepass_without(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user , data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request , fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user = request.user)
            return render(request , 'enroll/change1.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/login/')


def user_detail(request ,id):
    if request.user.is_authenticated:
        ur = User.objects.get(pk = id)
        fm = editadminprofil(instance=ur)
        return render(request , 'enroll/userdetail.html', {'form':fm})
    else:
        return HttpResponseRedirect("/login/")


def dashbord_data(request):
    if request.user.is_authenticated:
        return render(request , 'enroll/dashbord.html' , {'user':request.user.username})
    else:
        return HttpResponseRedirect('/login/')