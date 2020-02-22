from django.contrib import admin
from django.urls import path,include
from AccountsApp import views


urlpatterns = [
    path('home/', views.home),	
    
]
