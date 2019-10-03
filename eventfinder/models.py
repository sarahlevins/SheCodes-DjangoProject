from django.conf import settings
from django.db import models
from django.urls import reverse


class Event(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    category = models.ManyToManyField('Category', default='')
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, default='')
    venue = models.ForeignKey('Venue', on_delete=models.DO_NOTHING, default='')
    # attendees = 
    # photo = 

    def get_absolute_url(self):
        return reverse("eventfinder:event-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=50)
    venue_website = models.URLField(max_length=100, default='')
       
    def __str__(self):
        return self.name
