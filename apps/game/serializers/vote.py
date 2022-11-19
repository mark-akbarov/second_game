from rest_framework import serializers
from game.models.vote import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['user', 'collection', 'item']
        

class VoteCreateSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()