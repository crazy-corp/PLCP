"""PLCP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main import views
import main
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="home"),
    path("home",views.red),
    path('2',views.load2,name="load2"),
    path('3',views.load3,name="load3"),
    path('4',views.load4,name="load4"),
    path('data_csv',views.cs,name="csv"),
    path("transmit",views.transmit),
    path('index_state',views.index_state,name="index_state"),

]
