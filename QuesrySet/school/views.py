from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q

def home(re):
    # student_data = Student.objects.all()
    # student_data = Student.objects.filter(marks=99)

    # student_data = Student.objects.exclude(marks=99)

    # student_data = Student.objects.order_by('city')        #Alphabet ni value jove 'A' & 'a' both are dif.
    # student_data = Student.objects.order_by('-city')
    # student_data = Student.objects.order_by('?')

    # student_data = Student.objects.order_by('id').reverse()[:5]

    # student_data = Student.objects.values()
    # student_data = Student.objects.values('name','city')
    
    # student_data = Student.objects.values_list()
    # student_data = Student.objects.values_list('name')
    # student_data = Student.objects.values_list('name','id', named=True)

    # student_data = Student.objects.using('default')          #Setting ma jai ne jove database hase tya thi badlavi sakiye

    #student_data = Student.objects.dates('pass_date', 'year')


    #_____________________________________Second Table Start_____________________________________#

    qs1 = Student.objects.values_list('id','name' , named=True)
    qs2 = Teacher.objects.values_list('id','name' , named=True)

    # student_data = qs2.union(qs1)
    # student_data = qs2.union(qs1, all=True)

    # student_data = qs2.intersection(qs1)
    # student_data = qs1.intersection(qs2)

    # student_data = qs2.difference(qs1)
    # student_data = qs1.difference(qs2)


    #_____________________________________Operators_____________________________________#

    # student_data = Student.objects.filter(id=1) & Student.objects.filter(roll=7009)
    # student_data = Student.objects.filter(id=1 , roll=7009)
    # student_data = Student.objects.filter(   Q(id=1)   &   Q(roll=7009)   )

    # student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=7009)
    # student_data = Student.objects.filter(   Q(id=6)   |   Q(roll=7009)   )

    print("Return: " , student_data)
    print()
    print("SQL QUERY: ", student_data.query)
    return render(re, 'school/home.html', {'sd':student_data} )

def about(re):
    # student_data = Student.objects.get(pk=3)
    # student_data = Student.objects.get(name = 'jay')

    # student_data = Student.objects.order_by('name').first()
    # student_data = Student.objects.first()

    # student_data = Student.objects.order_by('name').last()
    # student_data = Student.objects.last()

    # student_data = Student.objects.latest('pass_date')

    # student_data = Student.objects.earliest('pass_date')

    # student_data = Student.objects.all()
    # print(student_data.exists())
    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data).exists())

    #student_data = Student.objects.create(name = 'navin',roll=3478,city='Nikal',marks=24,pass_date='2021-5-4')

    # student_data, created = Student.objects.get_or_create(name = 'dixita',roll=3267,city='Nikal',marks=24,pass_date='2021-5-4')
    # print(created)

    # student_data = Student.objects.filter(pk=11).update(name='shyam')
    # student_data = Student.objects.filter(marks=24).update(city='fail')

    # student_data ,created = Student.objects.update_or_create(id = 1,name='kohli' , defaults={'name':'jay'})
    # print(created)

    # objs=[
    #     Student(name='nakamo',roll=2389,city='navaribazar',marks=101,pass_date='2021-3-7'),
    #     Student(name='gando',roll=2457,city='bazar',marks=34,pass_date='2022-5-14'),
    #     Student(name='dayo',roll=1853,city='navari',marks=52,pass_date='2021-1-6'),
    # ]
    # student_data = Student.objects.bulk_create(objs)

    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = 'jetpur'
    # student_data = Student.objects.bulk_update(all_student_data , ['city'])

    # student_data = Student.objects.in_bulk([1,2])
    # print(student_data[1].name)
    # student_data = Student.objects.in_bulk()

    # student_data = Student.objects.get(pk=15).delete()
    # student_data = Student.objects.filter(marks = 24).delete()

    # student_data = Student.objects.all()
    # print(student_data.count())


    print("Return: " , student_data)    
    return render(re, 'school/about.html', {'sd':student_data} )
