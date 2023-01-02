from rest_framework import status
from rest_framework.test import APITestCase
from game.models.item import Item


class ItemTest(APITestCase):
    maxDiff = None
    
    @classmethod
    def setUpTestData(cls) -> None:
        cls.item1 = Item.objects.create(image='nike.jpg', title='NIKE')
        cls.item2 = Item.objects.create(image='adidas.jpg', title='adidas')
        cls.item3 = Item.objects.create(image='puma.jpg', title='PUMA')   
        
    def test_list(self):
        response = self.client.get('/api/v1/game/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_detail(self):
        response = self.client.get('/api/v1/game/items/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)