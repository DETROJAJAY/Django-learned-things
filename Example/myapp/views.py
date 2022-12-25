from django.shortcuts import render
from .models import Page,Post,Song,User
from datetime import date,time

def Home(re):
    return render(re, 'myapp/home.html')

def show_user_data(re):
    data1 = User.objects.all()
    data2 = User.objects.filter(email='jay@gmail.com')
    data3 = User.objects.filter(mypage__page_cat='cat 1')
    data4 = User.objects.filter(mypost__post_pdate__gt=date(2022,9,13))
    data5 = User.objects.filter(song__song_duration=3)

    return render(re, 'myapp/user.html',{'data1':data1 , 'data2':data2 , 'data3':data3 , 'data4':data4 , 'data5':data5})

def show_page_data(re):
    data1 = Page.objects.all()
    data2 = Page.objects.filter(page_cat='cat 3')
    data3 = Page.objects.filter(usr__email='dishant@gmail.com')

    return render(re, 'myapp/page.html',{'data1':data1 , 'data2':data2 , 'data3':data3})

def show_post_data(re):
    data1 = Post.objects.all()
    data2 = Post.objects.filter(post_pdate='2022-09-13')
    data3 = Post.objects.filter(usr__username='dishant')

    return render(re, 'myapp/post.html',{'data1':data1 , 'data2':data2 , 'data3':data3})

def show_song_data(re):
    data1 = Song.objects.all()
    data2 = Song.objects.filter(song_duration = 3)
    data3 = Song.objects.filter(usr__username = 'deep')

    return render(re, 'myapp/song.html',{'data1':data1 , 'data2':data2 , 'data3':data3})