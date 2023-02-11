from django.db import models

# Create your models here.
class Role(models.Model):
    RoleName = models.CharField(max_length=225)
    