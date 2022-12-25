from django.db import models



#__________________________________Abstract Base Class____________________________________#
from school.managers import CustomMnager2

class CommonInfo(models.Model):                     #Base Class
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    date = models.DateField()
    myQM = CustomMnager2()                          # Create Our Manager With Our Quesry Set from managers.py
    class Meta:                                     # Give permission for abstract it 
        abstract = True


class Student(CommonInfo):                          # Child class which inherite Base Class
    fees = models.IntegerField()
    date = None

class Teacher(CommonInfo):                          # Child class which inherite Base Class
    salary = models.IntegerField()

class Contractor(CommonInfo):                       # Child class which inherite Base Class
    date = models.DateTimeField()
    payment = models.IntegerField()




#__________________________________Multi-table Inheritance____________________________________#
from school.managers import CustomManager

class ExamCenter(models.Model):
    cname = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    myown = CustomManager()                     # Create custom manager by using function which created in "manager.py" 
    objects = models.Manager()


class Student2(ExamCenter):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()




#__________________________________Proxy Model____________________________________#

class ExamCenter2(models.Model):
    cname = models.CharField(max_length = 15)
    city = models.CharField(max_length=15)
    myobj = models.Manager()                            # Change the name of built in manager

class MyExamCenter(ExamCenter2):
    class Meta:
        proxy = True
        ordering = ['city']                   #Behavior Change kryo