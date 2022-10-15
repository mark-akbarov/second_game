from django.db import models
from core.base_model import BaseModel


class Collection(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Item(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pics/%Y/%m/%d')
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='item')

    def __str__(self) -> str:
        return self.title


class Vote(BaseModel):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='vote')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='vote') 
    vote = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.item__name   