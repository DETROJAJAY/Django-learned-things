from datetime import datetime, timedelta
from django.shortcuts import render,HttpResponse

def setcook(request):
    responce = render(request , 'student/setcookies.html' )
    # responce.set_cookie('lname' , 'heet' , expires=datetime.utcnow()+timedelta(days=3))
    responce.set_signed_cookie('name' , 'sonam' , salt = 'chup' ,expires=datetime.utcnow()+timedelta(days=3))
    return responce

def getcook(request):
    # nm = request.COOKIES['name']
    # nm = request.COOKIES.get('name',"Guest")
    nm = request.get_signed_cookie('name',salt='chup')
    return render(request , 'student/getcookies.html' , {'name':nm})

def delcook(request):
    responce = render(request , 'student/delcookies.html' )
    responce.delete_cookie('name')
    return responce


def setsess(request):
    request.session['name'] = 'jay'
    request.session['lname'] = 'sonam'
    # request.session.set_expiry(10)
    return render(request , 'student/setcookies.html')

def getsess(request):
    if 'name' in request.session:
        # nm = request.session['name']
        nm = request.session.get('name' , default='Guest')
        lnm = request.session.get('lname' , default='Guest2')
        request.session.modified = True
        key = request.session.keys()
        item = request.session.items()
        age = request.session.setdefault('age','26')
        return render(request , 'student/getcookies.html' , {'name':nm , 'lname':lnm ,'ky':key , 'it':item , 'ag':age})
    else:
        return HttpResponse("Your session has expired...")

def delsess(request):
    if 'name' and 'lname' in request.session:
        # del request.session['name']
        # del request.session['lname']
        request.session.flush()
        request.session.clear_expired()
    return render(request , 'student/delcookies.html')


def settestcook(request):
    request.session.set_test_cookie()
    return render(request , 'student/setcookies.html')

def gettestcook(request):
    tk = request.session.test_cookie_worked()
    return render(request , 'student/getcookies.html' , {'test':tk})

def deltestcook(request):
    request.session.set_test_cookie()
    return render(request , 'student/delcookies.html')


#page counter mate
def home(request):
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    return render(request , 'student/home.html' ,{'c':newcount})