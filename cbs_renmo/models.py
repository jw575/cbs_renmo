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

class Listing(models.Model):
    listing_id = models.IntegerField(max_length=30)
    listing_time = models.DateTimeField()
    seller_name = models.ForeignKey(User)
    RMB_amount = models.IntegerField(max_length=30)
    fx_rate = models.FloatField(max_length=30)

# Testing new version test test
