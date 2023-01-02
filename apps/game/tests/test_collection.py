from rest_framework import status
from rest_framework.test import APITestCase
from game.models.collection import Collection
from game.models.item import Item
from user.models.base import User


class CollectionTest(APITestCase):
    maxDiff = None
    
    @classmethod
    def setUp(cls) -> None:
        cls.item1 = Item.objects.create(title='item1', image='image.png')
        cls.item2 = Item.objects.create(title='item2', image='image.png')
        cls.item3 = Item.objects.create(title='item3', image='image.png')
        cls.collection1 = Collection(title='collection1')
        cls.collection1 = cls.collection1.save()
        cls.collection1 = cls.collection1.item.add(cls.item1.id, cls.item2.id, cls.item3.id)
        
    def test_list(cls):
        response = cls.client.get('/api/v1/game/collections/')
        cls.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_detail(cls):
        url = '/api/v1/collections/1/'
        response = cls.client.get(url)
        cls.assertEqual(response.status_code, status.HTTP_200_OK)