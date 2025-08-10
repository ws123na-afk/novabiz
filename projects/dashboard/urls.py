from django.urls import path
from .views import DashboardHome
urlpatterns=[path('',DashboardHome.as_view(),name='dashboard_home')]