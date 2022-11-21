from django.db import models
from game.models.collection import Collection


class Round(models.Model):
    collection = models.ManyToManyField(Collection)
