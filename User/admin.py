from django.contrib import admin

# Register your models here.
from .userModels import User

admin.site.register(User)