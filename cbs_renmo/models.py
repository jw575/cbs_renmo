# Contains database schema

# Must import models
from django.db import models

class User(models.Model):
    # Class inherits from generic class models.Model. Each table is a class definition
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)