from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    usr = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name = 'mypage')
    page_name = models.CharField(max_length=15)
    page_cat = models.CharField(max_length=15)
    page_pdate = models.DateField()

class Post(models.Model):
    usr= models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'mypost')
    post_title = models.CharField(max_length=15)
    post_cat = models.CharField(max_length=15)
    post_pdate = models.DateField()
     
class Song(models.Model):
    usr= models.ManyToManyField(User)
    song_name = models.CharField(max_length=15)
    song_duration = models.IntegerField()

    def written_by(self):
        return ','.join([str(i) for i in self.usr.all()])
