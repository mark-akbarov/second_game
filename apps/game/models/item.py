from django.db import models
from core.base_model import BaseModel
from file.models import File
from game.models.collection import Collection


class ItemCollection(BaseModel):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['item', 'collection']


class Item(BaseModel):
    collection = models.ManyToManyField(Collection, blank=True, through=ItemCollection)
    image = models.ForeignKey(File, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    votes = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title