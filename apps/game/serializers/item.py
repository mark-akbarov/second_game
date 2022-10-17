from rest_framework import serializers

from game.models.item import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', ]


class VoteSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()