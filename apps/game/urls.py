from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()

router.register('collections', CollectionViewSet)
router.register('items', ItemViewSet)

urlpatterns = [
    path('collection/<pk>/', VoteAPIView.as_view())
]

urlpatterns += router.urls
