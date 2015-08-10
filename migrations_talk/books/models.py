from django.db import models


# Create your models here.
class Book(models.Model):
    author_first_name = models.CharField(max_length=50)
    author_last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    number_pages = models.IntegerField()
    genre = models.CharField(max_length=15)
    publisher = models.CharField(max_length=50)
