from django.db import models

# Create your models here.

# class admin(models.Model):
#     username=models.CharField(max_length=30)
#     password=models.BigIntegerField()

class log(models.Model):
    name=models.CharField(max_length=40)
    palce=models.CharField(max_length=40)
    number=models.BigIntegerField()
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=60)
    password=models.BigIntegerField()

class File(models.Model):
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=30)
    image=models.CharField(max_length=60)

class Ajreg(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=60)
    email=models.CharField(max_length=80)
    password=models.BigIntegerField()






