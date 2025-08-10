# NovaBiz Max — All-in-One Business Platform (Django + Docker)

**Modules:** E‑commerce, Bookings, CRM/Leads, Marketplace (vendors), Payments (Stripe/PayPal adapters), Dashboard KPIs, PWA, WhatsApp, Quote Calculator, EN/AR.

## Quick Start (Local via Docker)
```bash
docker compose up --build -d
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser --email admin@example.com
docker compose exec web python manage.py loaddata demo_seed.json
# open http://localhost:8080
```
Admin: `/admin/`  |  Public demo login: `/accounts/demo-login/` (user: demouser / pass: demo123)

## Deploy on Render (free)
1. Push this repo to GitHub.
2. New **Web Service** on Render → **Deploy from Docker**.
3. Set env vars:
   - `DJANGO_SECRET_KEY` = (random long string)
   - `DJANGO_DEBUG` = `false`
   - `ALLOWED_HOSTS` = `*` (or your domain)
   - `NOVABIZ_BRAND` = `NovaBiz`
   - `NOVABIZ_WHATSAPP` = `056-0000000`
   - `STRIPE_PUBLIC_KEY` / `STRIPE_SECRET_KEY` (optional, for sandbox)
   - `PAYPAL_CLIENT_ID` / `PAYPAL_SECRET` (optional, for sandbox)
4. Add custom domain (e.g., `demo.novabiz.online`) and enable HTTPS.
5. Seed data:
```bash
python manage.py migrate
python manage.py loaddata demo_seed.json
```

## Feature Highlights
- **Store:** products, categories, cart, checkout, orders
- **Bookings:** services, slot booking, confirmations
- **CRM:** leads, statuses, admin view
- **Marketplace:** vendor model + views (skeleton dashboard)
- **Payments:** strategy layer with Stripe & PayPal adapters (stubs wired to demo checkout)
- **Dashboard:** basic KPIs (orders, bookings, leads)
- **PWA:** manifest + service worker
- **Growth:** WhatsApp button, quote calculator, blog placeholder
- **Bilingual:** EN/AR scaffolding + RTL hooks

> This scaffold is production‑friendly but intentionally lean. Extend per client.
