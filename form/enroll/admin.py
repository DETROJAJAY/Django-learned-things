from django.contrib import admin
# Register your models here.

from .models import student

@admin.register(student)
class MACS(admin.ModelAdmin):
    list_display = ('stuid','stuname','stumail','stupass')

# admin.site.register(student , MACS)
