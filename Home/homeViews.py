from django.shortcuts import render
from django.views import View
# Create your views here.

class Login(View):    
    def get(self,request):
        return render(request,"Login.html")
class Home(View):
    def get(self,request):
        return render(request,"Home.html")