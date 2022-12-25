from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    # user_name = models.ForeignKey(User, on_delete=models.CASCADE)       #For relationship between One User to Many Post
    # user_name = models.ForeignKey(User, on_delete=models.PROTECT)
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_title = models.CharField(max_length = 15)
    post_cat = models.CharField(max_length = 15)
    post_pdate = models.DateField()


class Song(models.Model):
    user_name=models.ManyToManyField(User)                  #For Many To Many Relationship
    song = models.CharField(max_length=30)
    song_duration = models.IntegerField()

    def Writen_by(self):
        return ','.join([str(p) for p in self.user_name.all()])