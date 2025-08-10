from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect
from django.views import View
User=get_user_model()
class DemoLoginView(View):
    def get(self, request):
        user,_=User.objects.get_or_create(username="demouser",defaults={"email":"demo@novabiz.online"})
        user.set_password("demo123"); user.save()
        auth=authenticate(request, username="demouser", password="demo123")
        if auth: login(request, auth)
        return redirect("dashboard_home")
class LogoutView(View):
    def get(self,request):
        logout(request); return redirect("home")
