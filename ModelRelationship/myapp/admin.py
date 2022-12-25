from django.contrib import admin
from.models import page,like

@admin.register(page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name','page_cat','page_publish_date','user_name']

@admin.register(like)
class likeAdmin(admin.ModelAdmin):
    list_display = ['panu','page_name','page_cat','page_publish_date','user_name','likes']