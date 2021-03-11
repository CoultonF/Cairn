from django.db import models

# Create your models here.
class TripReport(models.Model):
    trail = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    url = models.CharField(max_length=500)
    date = models.DateField()