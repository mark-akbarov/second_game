import collections
from requests import Response
from rest_framework import serializers
from game.models.item import ItemCollection
from game.models.vote import Vote


class VoteSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()

    class Meta:
        model = Vote
        fields = ['item_collection', 'user']    
        
        
class VoteCreateSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    collection_id = serializers.IntegerField()
    
    def create(self, validated_data):
        item_collection = ItemCollection.objects.get(item=self.item_id, collection=self.collection_id)
        user = self.request.user
        Vote.objects.create(item_collection=item_collection, user=user)
        return Response({"detail: successfully created"})