from django.db import models

# Create your models here.

class Officer(models.Model):
    officer_position = models.CharField("Officer Position", max_length=100)
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=100)
    email = models.EmailField("E-mail", max_length=300)
    phone_number = models.CharField("Phone Number", max_length=15, blank=True)

    def __str__(self):
        return self.officer_position
