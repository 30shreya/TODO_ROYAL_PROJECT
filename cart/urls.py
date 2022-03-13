from django.contrib import admin
from django.urls import include, path
from .views import CreatePayment,CreateCart

urlpatterns = [
    path('create_payment/', CreatePayment.as_view(), name='create_payment'),
    path('create_cart', CreateCart.as_view(), name='create_cart'),
    



]
