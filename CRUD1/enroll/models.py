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


    # def save(self,*args , **kwargs):
    #     account_sid = 'ACc937d539a486b78914b2b6c129d2eb2f'
    #     if len(str(self.phone)) == 10:
    #         auth_token = 'd2da85954fc5b2785d983642ac89c01b' 
    #         client = Client(account_sid, auth_token) 
            
    #         message = client.messages.create(    
    #                                     body="Hi it is working", 
    #                                     from_='+14255411703',    
    #                                     to=f'+91{self.phone}' 
    #                                 ) 
            
    #         print(message.sid)


    #     return super().save(*args , **kwargs)