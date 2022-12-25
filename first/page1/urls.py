from . import views
from django.urls import path

urlpatterns = [
    path('myurl/', views.jay),
    path('myurl1/', views.func),
    path('',views.home),
]