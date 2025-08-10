from django.conf import settings
def charge_with_stripe(amount_aed, metadata=None):
    # Stub: simulate success
    if not settings.STRIPE_SECRET_KEY: return {"ok": True, "ref": "STRIPE-DEMO-REF"}
    # Real Stripe SDK integration would go here.
    return {"ok": True, "ref": "STRIPE-LIVE-PLACEHOLDER"}

def charge_with_paypal(amount_aed, metadata=None):
    # Stub: simulate success
    if not settings.PAYPAL_CLIENT_ID or not settings.PAYPAL_SECRET: return {"ok": True, "ref": "PAYPAL-DEMO-REF"}
    # Real PayPal API integration would go here.
    return {"ok": True, "ref": "PAYPAL-LIVE-PLACEHOLDER"}
