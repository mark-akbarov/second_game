from rest_framework import serializers
from game.models.round import Round
from game.serializers.collection import CollectionMiniSerializer


class RoundSerializer(serializers.ModelSerializer):
    collection = CollectionMiniSerializer(many=True)
    class Meta:
        model = Round
        fields = ['id', 'collection']