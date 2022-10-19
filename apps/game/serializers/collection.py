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
    
    # def to_representation(self, instance):
    #     representation = super(CollectionSerializer, self).to_representation(instance)
    #     items = instance.items.all()
    #     dic = sorted({i.votes:v.title for i,v in zip(items, items)})
    #     representation['winner'] = dic[1]
    #     return representation


class CollectionListSerializer(serializers.ModelSerializer):
    item_set = ItemListSerializer(many=True)
    class Meta:
        model = Collection
        fields = ['id', 'title', 'item_set']
