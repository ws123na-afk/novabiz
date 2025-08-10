from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .adapters import charge_with_stripe, charge_with_paypal

@require_POST
def start_payment(request):
    amount = float(request.POST.get("amount", "0"))
    method = request.POST.get("method","stripe")
    if method == "paypal":
        res = charge_with_paypal(amount, {"source":"checkout"})
    else:
        res = charge_with_stripe(amount, {"source":"checkout"})
    return JsonResponse(res)
