
from django.urls import  path
from .tokenViews import TokenApi
urlpatterns = [
    path('api/token/', TokenApi.as_view(), name='LoginApi'),
]