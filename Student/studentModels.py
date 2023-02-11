from django.db import models
from User.userModels import User
# Create your models here.
class Student(models.Model):
    StudentName = models.CharField(max_length=225)
    StudentCode = models.CharField(max_length=225)
    Score = models.FloatField