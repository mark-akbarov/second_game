from django.db import models
from core.base_model import BaseModel
from user.models.base import User
from game.models.collection import Collection
from game.models.item import Item


class Vote(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)