from django.db import models

# Create your models here.

class Announcement(models.Model):
    title_text = models.CharField("Title", max_length=200)
    pub_date = models.DateTimeField("Date published", help_text="Click 'Today' and 'Now'")
    body_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.title_text

    class Meta():
        verbose_name = 'Announcement'
