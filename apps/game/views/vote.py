from rest_framework.generics import get_object_or_404, ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from game.serializers.vote import VoteSerializer, VoteCreateSerializer
from game.models.vote import Vote
from game.models.item import Item
from game.models.collection import Collection


class VoteListAPIView(ListAPIView):
    serializer_class = VoteSerializer

    def get_queryset(self):
        return Vote.objects.filter(user=self.request.user)


class CollectionVoteListAPIView(ListAPIView):
    serializer_class = VoteSerializer
    
    def get_queryset(self):
        collection = get_object_or_404(Collection, pk=self.kwargs['pk'])
        return Vote.objects.filter(collection=collection, user=self.request.user)
 

class VoteCreateAPIView(GenericAPIView):
    serializer_class = VoteCreateSerializer
    def post(self, request, pk):
        serializer = VoteCreateSerializer(data=request.data)
        if serializer.is_valid():
            item = get_object_or_404(Item, pk=serializer.validated_data['item_id'])
            collection = get_object_or_404(Collection, pk=pk, item=item)
            vote = Vote.objects.filter(user=request.user, collection=collection)
            if vote.exists():
                vote.delete()
                return Response({"detail": "vote removed"})
            else:
                vote = Vote.objects.create(user=request.user, collection=collection, item=item)
                vote.save()
                return Response({"detail": "vote added"})