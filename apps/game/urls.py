from django.urls import path
from rest_framework.routers import DefaultRouter

from game.views.collection import CollectionViewSet
from game.views.item import ItemViewSet, VoteAPIView


router = DefaultRouter()

router.register('collections', CollectionViewSet)
router.register('items', ItemViewSet)

urlpatterns = [
    path('collections/<pk>/vote/', VoteAPIView.as_view())
]

urlpatterns += router.urls
