from django.shortcuts import redirect
from django.views.generic import TemplateView
from .forms import LeadForm
class ContactView(TemplateView):
    template_name = "contact.html"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs); ctx["form"]=LeadForm(); return ctx
    def post(self, request, *args, **kwargs):
        form = LeadForm(request.POST)
        if form.is_valid(): form.save(); return redirect("contact_success")
        return self.render_to_response({"form": form})
class ContactSuccessView(TemplateView): template_name = "contact_success.html"
