from django.db import models
# from twilio.rest import Client 


class User(models.Model):
    name = models.CharField(max_length = 30)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField(max_length = 30)
    password = models.CharField(max_length =30)
    teacher = models.CharField(max_length = 15)

    def __str__(self):
        return str(self.result)
