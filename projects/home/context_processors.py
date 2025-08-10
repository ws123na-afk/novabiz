from django.conf import settings
def brand(request):
    return {
        "NOVABIZ_BRAND": getattr(settings,"NOVABIZ_BRAND","NovaBiz"),
        "NOVABIZ_WHATSAPP": getattr(settings,"NOVABIZ_WHATSAPP",""),
        "NOVABIZ_MARKETPLACE_ENABLED": getattr(settings,"NOVABIZ_MARKETPLACE_ENABLED",False),
        "BUSINESS_CHOICES":[("clinic","Clinic / Salon"),("restaurant","Restaurant / Café"),("store","Online Store")],
        "CURRENT_BUSINESS": request.session.get("current_business","clinic"),
        "STRIPE_PUBLIC_KEY": getattr(settings,"STRIPE_PUBLIC_KEY",""),
        "PAYPAL_CLIENT_ID": getattr(settings,"PAYPAL_CLIENT_ID",""),
    }
