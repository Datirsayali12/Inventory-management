from unittest import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Item
from rest_framework_simplejwt.tokens import RefreshToken

TOKEN_URL = reverse('token_obtain_pair')

class ItemAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        response = self.client.post(TOKEN_URL, {'username': 'testuser', 'password': 'testpass'})
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.item_data = {
            'name': 'Item1',
            'description': 'This is an item.',
            'quantity': 10,
            'price': 100.0
        }
        self.item = Item.objects.create(name='Item1', description='Sample Item', quantity=5, price=50)

    def test_create_item(self):
        response = self.client.post(reverse('item-create'), self.item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)
        self.assertEqual(response.data['name'], 'Item1')

    def test_get_item(self):
        response = self.client.get(reverse('item-detail', kwargs={'pk': self.item.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)

    def test_update_item(self):
        updated_data = {
            'name': 'Updated Item',
            'description': 'Updated description',
            'quantity': 20,
            'price': 150.0
        }
        response = self.client.put(reverse('item-detail', kwargs={'pk': self.item.id}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, updated_data['name'])

    def test_delete_item(self):
        response = self.client.delete(reverse('item-detail', kwargs={'pk': self.item.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)

    def test_item_not_found(self):
        response = self.client.get(reverse('item-detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

