# Generated by Django 2.2.1 on 2019-05-16 14:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0004_auto_20190516_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentorder',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
