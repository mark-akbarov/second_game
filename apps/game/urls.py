from django.urls import path
from rest_framework.routers import DefaultRouter
from game.views.round import RoundViewSet
from game.views.collection import CollectionViewSet
from game.views.item import ItemViewSet
from game.views.vote import VoteCreateAPIView, VoteListAPIView, CollectionVoteListAPIView
from game.views.winner import CollectionWinnerAPIView, CheckWinnerAPIView
from apps.game.views.send_mail import SendEmailView


router = DefaultRouter()

router.register('round', RoundViewSet)
router.register('collections', CollectionViewSet)
router.register('items', ItemViewSet)

urlpatterns = [
    path('collections/<pk>/vote/', VoteCreateAPIView.as_view()),
    path('collections/<pk>/check_win/', CheckWinnerAPIView.as_view()),
    path('collections/<pk>/winner_item/', CollectionWinnerAPIView.as_view()),
    path('collections/<pk>/vote_count/', CollectionVoteListAPIView.as_view()),
    path('vote_list/', VoteListAPIView.as_view()),
    path('send_email/', SendEmailView.as_view()),
]

urlpatterns += router.urls
