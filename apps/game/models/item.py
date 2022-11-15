from django.db import models
from core.base_model import BaseModel
from file.models import File
from game.models.collection import Collection


class Item(BaseModel):
    collection = models.ManyToManyField(Collection, blank=True)
    image = models.ForeignKey(File, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    votes = models.IntegerField()

    def __str__(self) -> str:
        return self.title