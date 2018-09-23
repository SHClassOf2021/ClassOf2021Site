from django.db import models
import datetime

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(help_text="Pick the date with the calendar icon")
    start_time = models.TimeField(help_text="Use military time i.e. 3p.m. is 15:00")
    end_time = models.TimeField(help_text="Use military time i.e. 6p.m. is 18:00")
    location = models.CharField(max_length=200)
    more_info = models.CharField(max_length=500)
    website = models.URLField(max_length=1000, blank=True)
    pub_date = models.DateTimeField("Publication date", help_text="Click 'Today' and 'Now'")

    def __str__(self):
        return self.name
