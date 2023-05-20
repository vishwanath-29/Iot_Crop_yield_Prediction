from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone_no = models.CharField(max_length=11)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)


