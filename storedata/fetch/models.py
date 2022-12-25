from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,blank = True)
    password = models.CharField(max_length=30)