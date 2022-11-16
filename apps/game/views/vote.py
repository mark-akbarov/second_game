from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from game.serializers.vote import VoteSerializer
from game.models.vote import Vote
from game.models.item import Item
from game.models.collection import Collection


class VoteCreateAPIView(APIView):
    def post(self, request, pk, item_pk):
        collection = get_object_or_404(Collection, pk=pk)
        item = get_object_or_404(Item, pk=item_pk)
        user = self.request.user
        vote = Vote.objects.filter(user=user, collection=collection)
        if vote.exists():
            vote.delete()
            return Response({"detail": "vote removed"})
        else:
            Vote.objects.create(user=user, collection=collection, item=item).save()
            return Response({"detail": "vote added"})
        

class VoteListAPIView(ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer