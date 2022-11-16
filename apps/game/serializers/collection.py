from django.forms import ValidationError
from rest_framework import serializers
from game.models.collection import Collection
from game.serializers.item import ItemListSerializer


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title',]

    def validate(self, attrs):
        title = attrs.get('title')
        if Collection.objects.filter(title=title).exists():
            raise ValidationError("Collection with that name already exists")
        return attrs


class CollectionListSerializer(serializers.ModelSerializer):
    item_set = ItemListSerializer(many=True)
    class Meta:
        model = Collection
        fields = ['id', 'title', 'item_set']
    
    def to_representation(self, instance):
        representation = super(CollectionListSerializer, self).to_representation(instance)
        collection = instance.item_set.all()
        votes = [i.vote_set.count() for i in collection]
        res = {k.title:v for k,v in zip(collection, votes)}
        representation['winner'] = sorted(res, key=res.get)[1]
        return representation

    def validate(self, data):
        if len(data['item_set']) != 3:
            raise serializers.ValidationError("Invalid number of items")
        return data