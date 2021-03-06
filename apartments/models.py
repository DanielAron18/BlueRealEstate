from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Model for apartment.
import agent
from agent.models import Agent


class Apartment(models.Model):
    postalcode = models.CharField(max_length=12)
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    bedrooms = models.IntegerField()
    size = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=255, default="description")
    agentid = models.ForeignKey(Agent, on_delete=models.CASCADE)
    def __str__(self):
        return self.location


class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    mainimage = models.BooleanField()
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class ApartmentOrder(models.Model):
    streetname = models.CharField(max_length=255, null=True)
    housenumber = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    postalcode = models.IntegerField(null=True)
    ssn = models.IntegerField(null=True)
    cardholdername = models.CharField(max_length=255)
    cardnumber = models.CharField(max_length=255)
    exp = models.IntegerField()
    cvv = models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
