from django.urls import path
from .homeViews import Login,Home
urlpatterns = [
    path('Login',Login.as_view()),
    path('Home',Home.as_view()),
]