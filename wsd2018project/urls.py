"""wsd2018project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from marjamehu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'home/', views.home, name='home'),
    path(r'marjamehu/', views.marjamehu, name='marjamehu'),
    path(r'home/peli', views.peli, name='peli'),
    path(r'accounts/', include('django.contrib.auth.urls')),
    path('register', views.register, name='register')
    #url(r'^login/$', auth_views.login, name='login')
]
