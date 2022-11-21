from django.contrib import admin
from game.models.collection import Collection
from game.models.item import Item
from game.models.vote import Vote
from game.models.round import Round


admin.site.register(Collection)
admin.site.register(Item)
admin.site.register(Vote)
admin.site.register(Round)