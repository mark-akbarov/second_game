from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
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
    
    
class Leaderboard(APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.all()[::-1]
        print(user)
        user_score = {i.username:i.score for i in user}
        print(user_score)
        winner_user = sorted(user_score, key=user_score.get)[1]
        print(winner_user)
        return Response({
                "user_score": user_score,
                "winner": winner_user,
             })
    