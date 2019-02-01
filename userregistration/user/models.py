from django.db import models

# Create your models here.

#User model
class user(models.Model):
    user_name = models.CharField(max_length=45, null=False, unique=True)
    email = models.EmailField(max_length=200, null=False, unique=True)
    password = models.CharField(max_length=45, null=False)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20)