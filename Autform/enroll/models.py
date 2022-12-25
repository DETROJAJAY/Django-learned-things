from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 15)
    desc = models.CharField(max_length=15)