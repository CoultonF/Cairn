from django.db import models
from django.utils import timezone

# Create your models here.

class Page(models.Model):

    url = models.CharField(max_length=250, unique=True)

    class Admin:
        pass