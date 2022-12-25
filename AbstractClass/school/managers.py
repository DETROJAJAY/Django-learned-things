from django.db import models


#Create Custom manager which also change in Query Set
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('cname')



#Create custom manager with our own quesry set
class CustomMnager2(models.Manager):
    def get_stu_age_range(self, r1, r2):
        return super().get_queryset().filter(age__range=(r1,r2))