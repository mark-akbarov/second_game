from rest_framework import serializers

from file.serializers import FileUrlSerializer
from game.models.item import Item, ItemCollection


class ItemSerializer(serializers.ModelSerializer):
    image = FileUrlSerializer()
    class Meta:
        model = Item
        fields = ['id', 'title', 'image', 'collection']


class ItemListSerializer(serializers.ModelSerializer):
    image = FileUrlSerializer()

    class Meta:
        model = Item
        fields = ['id', 'title', 'image', 'votes']
        

class ItemCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCollection
        fields = ['id', 'item', 'collection']