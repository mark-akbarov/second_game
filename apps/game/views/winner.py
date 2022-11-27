from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from game.models.collection import Collection
from game.models.vote import Vote


class CollectionWinnerAPIView(RetrieveAPIView):
    def get(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        item = collection.item.all()
        votes = {i.title:i.vote_set.filter(collection_id=collection).count() for i in item}
        winner = sorted(votes, key=votes.get)[1]
        return Response({"winner": winner})
    

class CheckWinnerAPIView(RetrieveAPIView):
    def get(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        item = collection.item.all()
        print(item)
        votes = {i.title:i.vote_set.filter(collection_id=collection).count() for i in item}
        winner = sorted(votes, key=votes.get)[1]
        user_vote = Vote.objects.filter(user=request.user, collection=collection)[0]
        user = request.user
        if str(winner) == str(user_vote.item):
            user.score += 10
            user.save()
            return Response({"detail": "correct!"})
        else:
            user = request.user
            user.score -= 5
            user.save()
            return Response({"detail": "incorrect"})