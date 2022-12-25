from django.urls import path
from . import views

urlpatterns = [
    path('rgtr/', views.showdata),
    path('succ/',views.tnk),
]
