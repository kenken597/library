import email
from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField('Name', max_length=64)
    last_name = models.CharField('Surname', max_length=64)
    birth_day = models.PositiveSmallIntegerField()

