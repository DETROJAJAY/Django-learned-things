from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Employee)
#admin.site.register(Employee_works)

@admin.register(Employee_works)
class empl(admin.ModelAdmin):
    list_display = ['name','workhours']
