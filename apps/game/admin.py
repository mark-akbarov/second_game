from django.contrib import admin
from game.models.collection import Collection
from game.models.item import Item

admin.site.register(Collection)
admin.site.register(Item)