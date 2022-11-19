from rest_framework import serializers
from file.serializers import FileUrlSerializer
from game.models.item import Item


class ItemSerializer(serializers.ModelSerializer):
    image = FileUrlSerializer()
    class Meta:
        model = Item
        fields = ['id', 'title', 'image', 'collection']


class ItemListSerializer(serializers.ModelSerializer):
    image = FileUrlSerializer()

    class Meta:
        model = Item
        fields = ['id', 'title', 'image']

    def to_representation(self, instance):
        representation = super(ItemListSerializer, self).to_representation(instance)
        representation['votes'] = instance.vote_set.count()
        return representation