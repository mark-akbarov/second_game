from django.db import models

from user.models.base import User
from core.base_model import BaseModel
from file.models import File
from game.models.collection import Collection

class Item(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ForeignKey(File, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='items')
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title