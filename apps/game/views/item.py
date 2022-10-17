from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


from game.serializers.item import ItemSerializer,VoteSerializer
from game.models.item import Item, Collection


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class VoteAPIView(APIView):
    def get(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            item = get_object_or_404(Item, pk=serializer.validated_data['item_id'], collection=collection)
            item.votes += 1
            item.save()
            return Response({"detail": "successfully added"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

