from django.urls import path
from .views import BookingView, BookingSuccessView
urlpatterns=[path('',BookingView.as_view(),name='booking'),path('success/',BookingSuccessView.as_view(),name='booking_success')]