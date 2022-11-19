from django.db import models
from core.base_model import BaseModel
from file.models import File


class Item(BaseModel):
    image = models.ForeignKey(File, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title