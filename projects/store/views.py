from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.conf import settings
from .models import Product, Order, OrderItem
from decimal import Decimal

def _get_order(request):
    oid = request.session.get('order_id')
    if oid:
        try: return Order.objects.get(id=oid, paid=False)
        except Order.DoesNotExist: pass
    order = Order.objects.create()
    request.session['order_id'] = order.id
    return order

class ProductListView(ListView):
    model = Product
    template_name = "store_list.html"
    context_object_name = "products"
    def get_queryset(self):
        qs = super().get_queryset()
        biz = self.request.session.get("current_business","clinic")
        if biz == "clinic":
            return qs.filter(category__name__in=["Skincare","Wellness"])
        if biz == "restaurant":
            return qs.filter(category__name__in=["Food","Beverage"])
        return qs

class CartView(TemplateView):
    template_name = "cart.html"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        order = _get_order(self.request)
        ctx["order"] = order
        ctx["items"] = order.items.select_related("product").all()
        return ctx

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order = _get_order(request)
    item, created = OrderItem.objects.get_or_create(order=order, product=product, defaults={"quantity":1,"price_each_aed":product.price_aed})
    if not created:
        item.quantity += 1; item.save()
    # recompute total
    total = Decimal(0)
    for it in order.items.all():
        total += it.quantity * it.price_each_aed
    order.total_aed = total; order.save()
    return redirect("cart")

def checkout_view(request):
    order = _get_order(request)
    return render(request, "checkout.html", {
        "order": order,
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        "PAYPAL_CLIENT_ID": settings.PAYPAL_CLIENT_ID,
    })

def checkout_success(request):
    # mark paid in demo
    oid = request.session.get('order_id')
    if oid:
        try:
            order = Order.objects.get(id=oid)
            order.paid = True
            order.payment_ref = "DEMO-" + str(order.id)
            order.save()
        except Order.DoesNotExist:
            pass
    return render(request, "checkout_success.html")
