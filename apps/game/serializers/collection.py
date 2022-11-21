from rest_framework import serializers
from game.models.collection import Collection
from game.serializers.item import ItemSerializer

class CollectionSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True)

    class Meta:
        model = Collection
        fields = ['id', 'title', 'item']


class CollectionListSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True)
    winner = serializers.SerializerMethodField()
    class Meta:
        model = Collection
        fields = ['id', 'title', 'item', 'winner']

    def get_winner(self, obj):
        item = obj.item.all()
        votes = {i.title:i.vote_set.filter(collection_id=obj).count() for i in item}
        winner = sorted(votes, key=votes.get)[1]
        return winner