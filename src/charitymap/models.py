from django.db import models
from django_google_maps import fields as map_fields

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    class Type(models.TextChoices):
        Store = '1',
        Bin = '2'

    type = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.Store
    ) 


class SuggestedLocation(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    votes = models.IntegerField()

    class Type(models.TextChoices):
        Store = '1',
        Bin = '2'

    type = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.Store
    )


class VotedLocations(models.Model):
    username = models.CharField(max_length=255)
    voted_at = models.DateTimeField(auto_now=True)
    geolocation = map_fields.GeoLocationField(max_length=100)