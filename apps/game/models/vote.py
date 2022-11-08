from django.db import models

from core.base_model import BaseModel
from user.models.base import User
from game.models.collection import Collection
from game.models.item import Item
from game.models.item import ItemCollection


class Vote(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_collection = models.ForeignKey(ItemCollection, on_delete=models.CASCADE)