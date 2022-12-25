from django.db import models
from django.contrib.auth.models import User             #ak class mate built in class j use kryo 6

class page(models.Model):
    # user_name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)    #aaya one relationship baanvi inbuilt class sathe
    # user_name = models.OneToOneField(User, on_delete=models.PROTECT, primary_key = True)
    # user_name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True, limit_choices_to={'is_staff':True})      #Signal aana mate banavelu 6
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    page_name = models.CharField(max_length = 90)
    page_cat = models.CharField(max_length=90)
    page_publish_date = models.DateField()


class like(page):
    panu = models.OneToOneField(page, on_delete=models.CASCADE, primary_key = True, parent_link=True)        #j class inheritance ma one-to-one relation bane aeni badele aapde hathe banavyu
    likes = models.IntegerField()