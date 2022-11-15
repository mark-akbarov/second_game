from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from game.models.vote import Vote
from game.models.item import Collection


class VoteCreateAPIView(APIView):
    def post(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        user = self.request.user
        vote = Vote.objects.filter(collection=collection, user=user)
        if vote.exists():
            vote.delete()
            return Response({"detail": "vote removed"})
        else:
            Vote.objects.create(collection=collection, user=user)
            return Response({"detail": "vote added"})