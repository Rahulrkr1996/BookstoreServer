from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    google_book_id = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    authors = models.CharField(max_length=100)
    image = models.TextField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
