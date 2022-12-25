from atexit import register
from django.contrib import admin
from school.models import Song, post

@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display=['post_title','post_cat','post_pdate','user_name']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song','song_duration','Writen_by']
