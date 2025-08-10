from django.urls import path
from .views import ProductListView, CartView, add_to_cart, checkout_view, checkout_success
urlpatterns = [
    path('', ProductListView.as_view(), name='store'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('checkout/success/', checkout_success, name='checkout_success'),
]
