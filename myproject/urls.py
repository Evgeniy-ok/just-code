"""myproject URL Configuration

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
from django.urls import path
from appshop import views
from django.views.generic import ListView, DeleteView
from django.contrib.auth import authenticate, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('profile', views.profile),
    path('posts', views.posts),
    path('newpost', views.newpost),
    path('post/<int:id>', views.post),
    path('editpost/<int:id>', views.editpost),
    path('saveeditpost/<int:id>', views.saveeditpost),
    path('deletepost/<int:id>', views.deletepost),
    path('export', views.export),
    path('download', views.download),
    path('registration', views.registration),
    path('login', views.login_user),
    path('logout', views.logout_user),

]
