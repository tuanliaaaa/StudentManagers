from django.urls import path
from .studentViews import StudentsByName
urlpatterns = [
    path('<str:name>',StudentsByName.as_view()),
]