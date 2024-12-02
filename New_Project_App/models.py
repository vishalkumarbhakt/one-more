from django.db import models

# Create your models here.
class Users_Data(models.Model):
    name =models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    age = models.SmallIntegerField()
    motherTongue = models.CharField(max_length=10)
    address = models.TextField()
    hobby = models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress = models.EmailField()