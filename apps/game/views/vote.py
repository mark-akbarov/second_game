from rest_framework.generics import CreateAPIView
from game.models.vote import Vote
from game.serializers.vote import VoteCreateSerializer


class VoteCreateAPIView(CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteCreateSerializer