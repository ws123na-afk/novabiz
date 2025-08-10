from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from store.models import Order
from booking.models import Booking
from crm.models import Lead

class DashboardHome(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/demo-login/'
    template_name = 'dashboard_home.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["orders_count"] = Order.objects.count()
        ctx["bookings_count"] = Booking.objects.count()
        ctx["leads_count"] = Lead.objects.count()
        return ctx
