from django.urls import path
from .views import MarketplaceHome
urlpatterns=[path('',MarketplaceHome.as_view(),name='marketplace_home')]