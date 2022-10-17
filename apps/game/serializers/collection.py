from django.forms import ValidationError
from rest_framework import serializers

from game.models.collection import Collection
from game.serializers.item import ItemSerializer



class CollectionSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Collection
        fields = ['id', 'title', 'items']

    def validate(self, attrs):
        title = attrs.get('title')
        if title:
            raise ValidationError("Collection with that name already exists")
        return attrs