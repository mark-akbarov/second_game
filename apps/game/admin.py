from django.contrib import admin
from game.models.collection import Collection
from game.models.item import Item, ItemCollection
from game.models.vote import Vote


admin.site.register(Collection)
admin.site.register(Item)
admin.site.register(ItemCollection)
admin.site.register(Vote)