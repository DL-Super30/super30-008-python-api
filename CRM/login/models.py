from django.db import models

# Create your models here.

class Loginuser(models.Model):

    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    