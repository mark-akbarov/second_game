from rest_framework import serializers
from game.models.collection import Collection
from game.serializers.item import ItemSerializer

class CollectionSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True)
    votes = serializers.SerializerMethodField()
    class Meta:
        model = Collection
        fields = ['id', 'title', 'item', 'votes']
    
    def get_votes(self, obj):
        item = obj.item.all()
        votes = {i.title:i.vote_set.filter(collection_id=obj).count() for i in item}
        return votes
    
    
class CollectionMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']