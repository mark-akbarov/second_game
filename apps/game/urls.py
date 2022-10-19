from django.urls import path
from rest_framework.routers import DefaultRouter

from game.views.collection import CollectionViewSet, CollectionListAPIView
from game.views.item import ItemViewSet
from game.views.vote import VoteAPIView

router = DefaultRouter()

router.register('collections', CollectionViewSet)
router.register('items', ItemViewSet)

urlpatterns = [
    path('collections_list/', CollectionListAPIView.as_view()),
    path('collections/<pk>/vote/', VoteAPIView.as_view()),
]

urlpatterns += router.urls
