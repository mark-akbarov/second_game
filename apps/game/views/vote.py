from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from game.models.collection import Collection
from game.models.vote import Vote
from game.serializers.vote import VoteSerializer
from game.serializers.item import Item


class VoteAPIView(APIView):
    def get(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            item = get_object_or_404(Item, pk=serializer.validated_data['item_id'], collection=collection)
            if Vote.objects.filter(item=item, user=self.request.user.id).exists():
                return Response({"detail: You have already voted"})
            else: 
                item.votes += 1
                item.save()
                vote = Vote(item=item, user=self.request.user)
                vote.save()
            return Response({"detail": "successfully added"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

