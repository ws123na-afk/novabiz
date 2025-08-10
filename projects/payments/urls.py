from django.urls import path
from .views import start_payment
urlpatterns=[path('start/', start_payment, name='start_payment')]