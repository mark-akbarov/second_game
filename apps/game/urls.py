from django.urls import path
from rest_framework.routers import DefaultRouter

from game.views.collection import CollectionViewSet, CollectionListAPIView
from game.views.item import ItemViewSet, ItemCollectionViewSet
from game.views.vote import VoteCreateAPIView

router = DefaultRouter()

router.register('collections', CollectionViewSet)
router.register('items', ItemViewSet)
router.register('item_collections', ItemCollectionViewSet)

urlpatterns = [
    path('collections_list/', CollectionListAPIView.as_view()),
    path('collections/vote/', VoteCreateAPIView.as_view()),
]

urlpatterns += router.urls
