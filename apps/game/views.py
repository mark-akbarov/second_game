from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


from .serializers import *
from .models import *


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class VoteAPIView(APIView):
    def get(self, request, pk):
        collection = get_object_or_404(CollectionSerializer, pk=pk)
        try:
            voted_item = collection.items.get(pk=request.POST['items'])
        except (KeyError, Item.DoesNotExist):
            return Response({'collection': collection,'error_message': "You didn't select a choice."})
        else:
            voted_item.votes += 1
            voted_item.save()
        return Response({"detail": "successfully added"})

