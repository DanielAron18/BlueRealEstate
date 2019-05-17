from django.db import models


# Create your models here.
class Search(models.Model):
    zip = models.CharField(max_length=12)
    location = models.CharField(max_length=255)