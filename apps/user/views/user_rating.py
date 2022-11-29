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
        user = User.objects.all()
        user_dict = {i.username:i.score for i in user}
        leaderboard = {k: user_dict[k] for k in sorted(user_dict, key=user_dict.get, reverse=True)}
        return Response({"leaderboard": leaderboard})
    

class LeaderboardWinner(APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        user_dict = {i.score:i.username for i in user}
        user_votes = [i.score for i in user]
        user_votes.sort(reverse=True)
        second_place = user_votes[1]
        leaderboard_winner = user_dict[second_place]
        return Response({"leaderboard_winner": leaderboard_winner})