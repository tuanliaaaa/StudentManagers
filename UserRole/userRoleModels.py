from django.db import models
from Role.roleModels import Role
from User.userModels import User
# Create your models here.
class UserRole(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Role = models.ForeignKey(Role,on_delete=models.CASCADE)