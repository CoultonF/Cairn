from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.TextField()
    report_count = models.IntegerField()

class TripReport(models.Model):
    date_of_trip = models.DateField()
    location = models.CharField(max_length=50, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    url = models.TextField()
    text = models.TextField()
    distance = models.DecimalField(decimal_places=1, max_digits=4)
    duration = models.TimeField()
    elevation = models.IntegerField()
    display_img = models.ImageField()
    images_count = models.IntegerField()
    activity = models.TextField()
    terrain_class = models.IntegerField()