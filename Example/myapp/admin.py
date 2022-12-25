from django.contrib import admin

from myapp.models import Page, Post, Song

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['page_name','page_cat','page_pdate','usr']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title','post_cat','post_pdate','usr']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name','song_duration','written_by']
