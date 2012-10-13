from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField()

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    movie = models.ForeignKey(Movie)
    