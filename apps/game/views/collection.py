from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from game.serializers.collection import CollectionSerializer, CollectionListSerializer
from game.models.collection import Collection


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionListAPIView(ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionListSerializer