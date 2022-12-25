from . import views
from django.urls import path

urlpatterns = [
    path('myurl2/', views.func),
    path('myurl3/',views.func2)
]