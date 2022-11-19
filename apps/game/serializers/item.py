from rest_framework import serializers
from file.serializers import FileUrlSerializer
from game.models.item import Item


class ItemSerializer(serializers.ModelSerializer):
    image = FileUrlSerializer()
    class Meta:
        model = Item
        fields = ['id', 'title', 'image']