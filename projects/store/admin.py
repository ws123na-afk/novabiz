from django.contrib import admin
from .models import Product, Category, Order, OrderItem
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=("id","created_at","total_aed","paid","payment_ref")
    inlines=[OrderItemInline]
admin.site.register(Product)
admin.site.register(Category)
