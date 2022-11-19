from rest_framework import serializers
from game.models.collection import Collection
from game.serializers.item import ItemSerializer

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class CollectionListSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True)
    class Meta:
        model = Collection
        fields = ['id', 'title', 'item']
        
    def to_representation(self, instance):
        representation = super(CollectionListSerializer, self).to_representation(instance)
        item = instance.item.all()
        votes = {i.title:i.vote_set.filter(collection_id=instance).count() for i in item}
        winner = sorted(votes, key=votes.get)[1]
        representation['votes'] = votes
        representation['winner'] = winner
        return representation