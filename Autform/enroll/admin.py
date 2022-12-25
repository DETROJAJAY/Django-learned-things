from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlockModelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']
