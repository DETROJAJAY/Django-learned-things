from django.urls import path
from . import views

urlpatterns = [
    path('field/', views.all_fields),
    path('done/' , views.AD)
]
