from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=60,blank=False)
    email=models.EmailField(blank=False)
    password=models.CharField(max_length=60,blank=False)


    


    