from django.shortcuts import redirect
from django.views.generic import TemplateView
from .forms import BookingForm
from .models import Service
class BookingView(TemplateView):
    template_name = "booking.html"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs); ctx["form"]=BookingForm(); ctx["services"]=Service.objects.all(); return ctx
    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid(): form.save(); return redirect("booking_success")
        return self.render_to_response({"form": form, "services": Service.objects.all()})
class BookingSuccessView(TemplateView): template_name = "booking_success.html"
