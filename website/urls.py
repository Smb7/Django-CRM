from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'), For a seperate page
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'), # step 1 -> now we go to views.py 
]
