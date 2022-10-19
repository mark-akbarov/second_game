from django.db import models

from core.base_model import BaseModel
from user.models.base import User
from game.models.item import Item


class Vote(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['item', 'user']