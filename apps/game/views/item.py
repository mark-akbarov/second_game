from rest_framework.viewsets import ModelViewSet
from game.serializers.item import ItemSerializer
from game.models.item import Item


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer