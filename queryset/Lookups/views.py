from itertools import count
from django.shortcuts import render
from .models import Student
from datetime import date,time
from django.db.models import Avg,Sum,Min,Max,Count,Q


def Home(re):
    # student_data = Student.objects.filter(name__exact = 'jay')
    # student_data = Student.objects.filter(name__iexact = 'Jay')

    # student_data = Student.objects.filter(name__contains = 'ee')
    # student_data = Student.objects.filter(name__icontains = 'EE')

    # student_data = Student.objects.filter(id__in = [1,3,6])

    # student_data = Student.objects.filter(marks__in = [99])

    # student_data = Student.objects.filter(marks__gt = 90)

    # student_data = Student.objects.filter(marks__gte = 90)

    # student_data = Student.objects.filter(marks__lt = 90)

    # student_data = Student.objects.filter(marks__lte = 90)

    # student_data = Student.objects.filter(name__startswith = 'm')
    # student_data = Student.objects.filter(name__istartswith = 'M')

    # student_data = Student.objects.filter(name__endswith = 'p')
    # student_data = Student.objects.filter(name__iendswith = 'P')

    # student_data = Student.objects.filter(passdate__range=('2020-03-2','2022-3-3'))

    # student_data = Student.objects.filter(admdatetime__date = date(2020,3,7))
    # student_data = Student.objects.filter(admdatetime__date__gt = date(2020,3,7))

    # student_data = Student.objects.filter(passdate__year = 2020) 
    # student_data = Student.objects.filter(passdate__year__gt = 2020)
    # student_data = Student.objects.filter(passdate__year__gte = 2020)

    # student_data = Student.objects.filter(passdate__month__gte = 3)

    # student_data = Student.objects.filter(passdate__day__lte = 7)

    # student_data = Student.objects.filter(passdate__week__gt = 24) 

    # student_data = Student.objects.filter(passdate__week_day = 3)       #dar week na day 3(wedasnday) no data

    # student_data = Student.objects.filter(admdatetime__time__gt= time(12,00))

    # student_data = Student.objects.filter(admdatetime__hour__gt= 10)

    # student_data = Student.objects.filter(admdatetime__minute__gt= 30)

    # student_data = Student.objects.filter(admdatetime__second = 40)

    # student_data = Student.objects.filter(roll__isnull =True)



    print("Return: ",student_data)
    print()
    print("SQl Quesry: ", student_data.query)
    return render(re, 'Lookups/home.html', {'sd':student_data})


def Aggr(re):
    student_data = Student.objects.all()

    average = student_data.aggregate(Avg('marks'))
    sum = student_data.aggregate(Sum('marks'))
    mini = student_data.aggregate(Min('marks'))
    maxi = student_data.aggregate(Max('marks'))
    total = student_data.aggregate(Count('marks'))



    print("Return: ", student_data)
    print()
    print("SQl Quesry: ", student_data.query)
    return render(re, 'Lookups/agrrigate.html', {'av':total})


def Qbhai(re):

    # student_data = Student.objects.filter(Q(id=6) & Q(roll=256))
    # student_data = Student.objects.filter(Q(id=6) | Q(roll=103))
    student_data = Student.objects.filter( ~Q(id=6) )

    print("Return: ", student_data)
    print()
    print("SQl Quesry: ", student_data.query)
    return render(re, 'Lookups/qbhaii.html', {'qbhai':student_data})


def LQS(re):
    
    # student_data = Student.objects.all()[:3] 
    # student_data = Student.objects.all()[2:5] 
    student_data = Student.objects.all()[:6:2] 


    print("Return: ", student_data)
    print()
    #print("SQl Quesry: ", student_data.query)          #last ma list return kre atle aa nai chale[:6:2]
    return render(re, 'Lookups/qbhaii.html', {'qbhai':student_data})