from django.urls import path,register_converter
from . import views,converters

register_converter(converters.FourDigitConvter , 'myown')

urlpatterns = [path('session/<myown:my_id>/', views.show_data , name="detail"),
            path('session/<my_id>/<int:my_subid>/', views.show_subdata , name="subdetail"),
        ]