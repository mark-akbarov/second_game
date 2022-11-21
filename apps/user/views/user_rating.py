from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from user.serializers.me import UserSerializer, UserScoreSerializer
from user.models.base import User


class UserRatingListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['score', 'id', 'username']
    ordering = ['score']


class UserScoreRatingAPIView(ListAPIView):
    serializer_class = UserScoreSerializer
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)