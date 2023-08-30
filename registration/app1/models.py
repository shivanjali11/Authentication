from django.db import models
class Child(models.Model):
    child_name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    remarks = models.TextField()
    picture = models.ImageField(upload_to='child_pictures/', null=True, blank=True)

# Create your models here.
# app1/models.py

class UserRegistration(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)

