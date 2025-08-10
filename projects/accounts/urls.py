from django.urls import path
from .views import DemoLoginView, LogoutView
urlpatterns=[
    path('demo-login/', DemoLoginView.as_view(), name='demo_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
