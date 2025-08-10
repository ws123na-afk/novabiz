from django.views.generic import TemplateView, View
from django.shortcuts import redirect

class HomeView(TemplateView):
    template_name = "home.html"

class SwitchBusinessView(View):
    def get(self, request, slug):
        request.session["current_business"] = slug
        return redirect("home")
