from django.db import models
from core.base_model import BaseModel


class Item(BaseModel):
    image = models.ImageField()
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title