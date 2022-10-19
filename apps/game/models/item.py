from django.db import models
from core.base_model import BaseModel
from file.models import File
from game.models.collection import Collection

class Item(BaseModel):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    image = models.ForeignKey(File, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title