"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from page1 import views as fs
from page2 import views as sc

page1_pattern  = [
        path('myurl/', fs.jay),
        path('myurl1/', fs.func),
        path('',fs.home),    
    ]

page2_pattern = [
        path('myurl2/', sc.func),
        path('myurl3/',sc.func2)
    ]


urlpatterns = [
    path('admin/', admin.site.urls),

    #path('url/',include('page1.urls'))
    path('url/',include(page1_pattern)),

    #path('url/',include('page2.urls'))
    path('url2/',include(page2_pattern)),
]
