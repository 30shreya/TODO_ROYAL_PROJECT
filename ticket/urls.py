from django.contrib import admin
from django.urls import include, path
from ticket import views

urlpatterns = [
    path('add/',views.add),
    path('view/',views.view),
    path('page/',views.mainpage),
]
   

