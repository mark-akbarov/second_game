from django.contrib import admin
from game.models import Vote, Item, Collection

admin.site.register(Item)
admin.site.register(Vote)
admin.site.register(Collection)