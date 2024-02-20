from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10, blank=True)
    password = models.CharField(max_length=255)
    age = models.IntegerField(blank=True)
