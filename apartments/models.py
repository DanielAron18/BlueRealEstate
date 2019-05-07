from django.db import models
from django.contrib.postgres.fields import ArrayField


# Model for apartment.


class Apartments(models.Model):
    name = models.CharField(max_length=255)
    postalcode = models.CharField(max_length=12)
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    bedrooms = models.IntegerField(max_length=2)
    size = models.IntegerField(max_length=4)
    price = models.IntegerField(max_length=9)
    images = ArrayField(models.URLField(max_length=255))

