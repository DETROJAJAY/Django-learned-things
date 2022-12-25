from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.sd),
    path('done/' , views.AD),
]