from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
    	return self.name

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    movie = models.ForeignKey(Movie)

    def __unicode__(self):
    	return "%s (%f, %f)" % (self.movie.name, self.latitude, self.longitude)
