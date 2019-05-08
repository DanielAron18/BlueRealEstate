from django.db import models
from django.contrib.postgres.fields import ArrayField


# Model for apartment.


class Agent(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=255)
    admin = models.BooleanField(default=False)
    startdate = models.DateField()
    profilepicture = models.CharField(max_length=255, blank=True)
    cellphone = models.CharField(max_length=15)
    workphone = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    license = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rating = models.IntegerField(max_length=1)
    comments = ArrayField(models.CharField(max_length=140))
