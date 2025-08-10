from django.db import models
class Lead(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="New", choices=[("New","New"),("In Progress","In Progress"),("Closed","Closed")])
    def __str__(self): return f"{self.name} - {self.status}"
