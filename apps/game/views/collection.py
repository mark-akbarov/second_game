from rest_framework.viewsets import ModelViewSet
from game.serializers.collection import CollectionSerializer
from game.models.collection import Collection


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer