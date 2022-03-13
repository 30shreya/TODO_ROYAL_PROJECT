from django.contrib import admin
from django.urls import include, path
from employee import views

urlpatterns = [
    path('add/',views.addEmployee),
    path('view/',views.viewEmployee),
    
    
]
   