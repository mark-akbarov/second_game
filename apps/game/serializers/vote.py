from rest_framework import serializers
from game.models.vote import Vote


class VoteSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()

    class Meta:
        model = Vote
        fields = ['collection', 'user']