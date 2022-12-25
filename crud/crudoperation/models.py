from ctypes import addressof
import email
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Employee(models.Model):
    userid = models.IntegerField(null = True)
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Employee_works(models.Model):
    fk = models.ForeignKey(Employee, on_delete=models.CASCADE)

    @property
    def name(self):
        return self.fk.name
    workhours = models.IntegerField()
    
    def written_by(self):
        return ",".join([str(p) for p in self.Employee.all()])


    
