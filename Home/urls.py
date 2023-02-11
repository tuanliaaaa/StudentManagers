from django.urls import path
from .homeViews import Login
urlpatterns = [
    path('Login',Login.as_view()),
]