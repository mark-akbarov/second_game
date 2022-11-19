from django.db import models
from core.base_model import BaseModel
from game.models.item import Item


class Collection(BaseModel):
    title = models.CharField(max_length=255)
    item = models.ManyToManyField(Item, blank=True)

    def __str__(self) -> str:
        return self.title