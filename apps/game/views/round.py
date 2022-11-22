from rest_framework.viewsets import ModelViewSet
from game.serializers.round import RoundSerializer
from game.models.round import Round


class RoundViewSet(ModelViewSet):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer