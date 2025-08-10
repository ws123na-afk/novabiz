from django import forms
from .models import Booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name","phone","service","date","time","notes"]
        widgets = {"date": forms.DateInput(attrs={"type":"date"}), "time": forms.TimeInput(attrs={"type":"time"})}
