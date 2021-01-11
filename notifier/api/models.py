from django.db import models


# Create your models here.
class MangaList(models.Model):

    name = models.TextField(max_length=100)
    url = models.URLField(max_length=300)
    updated = models.BooleanField(default=False)
