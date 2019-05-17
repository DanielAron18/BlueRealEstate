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
    bedrooms = models.IntegerField(max_length=2)
    size = models.IntegerField(max_length=4)
    price = models.IntegerField(max_length=9)
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
    postalcode = models.IntegerField(max_length=12, null=True)
    ssn = models.IntegerField(max_length=20, null=True)
    cardholdername = models.CharField(max_length=255)
    cardnumber = models.CharField(max_length=255)
    exp = models.DateField(max_length=8)
    cvv = models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
