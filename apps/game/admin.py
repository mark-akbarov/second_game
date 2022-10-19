from django.contrib import admin
from game.models.collection import Collection
from game.models.item import Item
from game.models.vote import Vote


admin.site.register(Collection)
admin.site.register(Item)
admin.site.register(Vote)