"""
URL configuration for user_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('accesslogin/',views.accesslogin),
    path('login/',views.login,name="login"),
    #Dashboards
    path('adminscreen/', views.adminscreen, name="adminscreen"),
    path('userscreen/', views.userscreen, name="userscreen"),
    path('users/', views.view_users, name="view_users"),
    path('user/details/', views.user_details, name="user_details"),
    path('user/add/', views.add_user, name="add_user"),
    path('user/remove/', views.remove_user, name="remove_user"),
    path('logout/',views.logout, name="logout"),
    path('set-role/', views.set_role, name='set_role'),

]
