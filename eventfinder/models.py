from django.conf import settings
from django.db import models
from django.urls import reverse

from users.models import User


class Event(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    category = models.ManyToManyField('Category', default='')
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, default='')
    venue = models.ForeignKey('Venue', on_delete=models.DO_NOTHING, default='')
    attendees = models.ManyToManyField(User, related_name='attendees', symmetrical=False, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to ='event_photos', blank=True)

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
    venue_photo = models.ImageField(upload_to='venue_photos', blank=True)
       
    def __str__(self):
        return self.name
