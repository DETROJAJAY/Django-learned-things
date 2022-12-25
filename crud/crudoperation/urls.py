from django import views
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('my/',views.open),
    path('add',views.add,name='add'),
    path('edit',views.edit,name='edit'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]