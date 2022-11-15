from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from game.serializers.vote import VoteSerializer
from game.models.vote import Vote
from game.models.item import Item
from game.models.collection import Collection


class VoteCreateAPIView(APIView):
    def post(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        user = self.request.user
        vote = Vote.objects.filter(collection=collection, user=user)
        if vote.exists():
            vote.delete()
            return Response({"detail": "vote removed"})
        else:
            serializer = VoteSerializer(data=request.data)
            Vote.objects.create(collection=collection, user=user)
            if serializer.is_valid():
                item = get_object_or_404(Item, pk=serializer.validated_data['item_id'], collection=collection)
                print(item)
                item.votes += 1
                return Response({"detail": "vote added"})