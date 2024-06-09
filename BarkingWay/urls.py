"""
URL configuration for BarkingWay project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from homepage.views import *
from django.conf.urls import handler404

handler404 = 'homepage.views.custom_404'
handler500 = 'homepage.views.custom_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home_view, name="home"),
    path('d_o_profile/', include('d_o_profile.urls'), name='profile'),
    path('breeds/', include('breeds.urls'), name='breeds'),
    path('events/', include('events.urls'), name='events'),
    path('petcare/', include('petcare.urls'), name='petcare'),
]
