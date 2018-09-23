from django.db import models

# Create your models here.

class FlickrAlbums(models.Model):
    name = models.CharField(max_length=100, help_text="Name of photo album")
    link = models.URLField(max_length=1000, help_text="Share Link to the Flickr album")

    class Meta():
        verbose_name = 'Photo Album'
        verbose_name_plural = 'Photo Albums'

    def __str__(self):
        return self.name
