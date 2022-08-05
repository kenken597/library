from django.db import models

# Create your models here.
class User(models.Model):
     User_name = models.CharField('User name', max_length=64)
     first_name = models.CharField('Name', max_length=64)
     last_name = models.CharField('Surname', max_length=64)
     birth_day = models.PositiveSmallIntegerField()
     email= models.CharField('Email', max_length=64, unique=True)