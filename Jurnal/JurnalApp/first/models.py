from django.db import models
from faker import Faker

class Person(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=100)
