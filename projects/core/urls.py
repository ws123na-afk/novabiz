from django.contrib import admin
from django.urls import path, include
from home.views import HomeView, SwitchBusinessView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('switch/<slug:slug>/', SwitchBusinessView.as_view(), name='switch_business'),
    path('store/', include('store.urls')),
    path('booking/', include('booking.urls')),
    path('crm/', include('crm.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('accounts/', include('accounts.urls')),
    path('payments/', include('payments.urls')),
]
