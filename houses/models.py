from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class House(models.Model):

    """ House Definition for House """

    name = models.CharField(max_length=140)
    price = models.PositiveBigIntegerField(help_text="Positive Numbers Only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
