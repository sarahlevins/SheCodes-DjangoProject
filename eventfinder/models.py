from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    # photo = 
    # venue = 
    # category = 
    # host = 
    # attendees = 

    # def get_absolute_url(self):
    #     return reverse("eventfinder:event", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
