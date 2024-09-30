from django.db import models

# Create your models here.
class Courses(models.Model):

    Course_Image=models.ImageField()
    Course_Name=models.CharField(max_length=200)
    Course_Fee=models.DecimalField(max_digits=12,decimal_places=2)
    Description=models.TextField(max_length=300)
    Course_Brochure=models.FileField()
    