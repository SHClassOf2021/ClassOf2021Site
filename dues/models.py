from django.db import models
# Create your models here.

class Dues(models.Model):
    title = models.CharField(max_length=30)
    announcement = models.CharField(max_length=50)

    class Meta():
        verbose_name = "Dues Announcement"

    def __str__(self):
        return self.title
