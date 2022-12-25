from . import views
from django.urls import path

urlpatterns = [
    path('myurl/', views.jay),
    path('myurl1/', views.jay2),
]