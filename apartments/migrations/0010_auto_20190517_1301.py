# Generated by Django 2.2.1 on 2019-05-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0009_auto_20190516_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentorder',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='apartmentorder',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='apartmentorder',
            name='housenumber',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='apartmentorder',
            name='postalcode',
            field=models.IntegerField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='apartmentorder',
            name='ssn',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='apartmentorder',
            name='streetname',
            field=models.CharField(max_length=255, null=True),
        ),
    ]