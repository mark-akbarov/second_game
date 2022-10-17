from django.db import models
from core.base_model import BaseModel


class Collection(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title