from django.urls import path
from rest_framework.routers import DefaultRouter
from game.views.collection import CollectionViewSet, CollectionListAPIView
from game.views.item import ItemViewSet
from game.views.vote import VoteCreateAPIView, VoteListAPIView, CollectionVoteListAPIView
from game.views.winner import WinnerAPIView, UserWinnerAPIView


router = DefaultRouter()

router.register('collections', CollectionViewSet)
router.register('items', ItemViewSet)

urlpatterns = [
    path('collections_list/', CollectionListAPIView.as_view()),
    path('collections/<pk>/vote/', VoteCreateAPIView.as_view()),
    path('collections/<pk>/winner_item/', WinnerAPIView.as_view()),
    path('collections/<pk>/check_win/', UserWinnerAPIView.as_view()),
    path('vote_list/', VoteListAPIView.as_view()),
    path('collections/<pk>/vote_list/', CollectionVoteListAPIView.as_view()),
]

urlpatterns += router.urls
