from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=225)
    Password = models.CharField(max_length=225)