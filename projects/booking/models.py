from django.db import models
class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price_aed = models.DecimalField(max_digits=10, decimal_places=2)
    duration_minutes = models.PositiveIntegerField(default=60)
    def __str__(self): return self.name
class Booking(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.name} - {self.service.name} ({self.date} {self.time})"
