# search/models.py
from django.db import models


class Search(models.Model):
    website = models.CharField(max_length=500)
    results = models.TextField()

    def __str__(self):
        return self.website