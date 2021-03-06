from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Model for User.


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    socialsecurity = models.CharField(max_length=255)
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=255)
    startdate = models.DateField()
    profilepicture = models.CharField(max_length=255, blank=True)
    cellphone = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    searchhistory = ArrayField(models.CharField(max_length=140, default=list))
