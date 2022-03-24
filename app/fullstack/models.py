from django.db import models
from pkg_resources import AvailableDistributions

from fullstack.views import speakers

# Create your models here.
class Speaker(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    avatar = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}.{self.name} {self.lastname}"
        