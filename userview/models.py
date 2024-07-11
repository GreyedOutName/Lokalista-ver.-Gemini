from django.db import models

# Create your models here.
class Foodlist(models.Model):
    region = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    market = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    item = models.CharField(max_length=120)
    unit = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    currency = models.CharField(max_length=120)
    price = models.IntegerField()