from rest_framework.viewsets import ModelViewSet

from game.serializers.item import ItemSerializer, ItemCollectionSerializer
from game.models.item import Item, ItemCollection


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    

class ItemCollectionViewSet(ModelViewSet):
    queryset = ItemCollection.objects.all()
    serializer_class = ItemCollectionSerializer