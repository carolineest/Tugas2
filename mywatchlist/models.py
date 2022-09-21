from django.db import models

# Create your models here.
class mywatchlist(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    watched = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    review = models.TextField()