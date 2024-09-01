from rest_framework.test import APITestCase
from rest_framework import status
from collection.models import Collection
from django.contrib.auth.models import User
import factory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Faker('user_name')
    email = factory.Faker('email')

class CollectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Collection
    name = factory.Faker('word')
    owner = factory.SubFactory(UserFactory)

class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item
    title = factory.Faker('sentence')
    collection = factory.SubFactory(CollectionFactory)

class CollectionAPIViewTests(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.collection = CollectionFactory(owner=self.user)
        self.item = ItemFactory(collection=self.collection)
        self.client.force_authenticate(user=self.user)

    def test_get_collection_with_items(self):
        response = self.client.get(f'/api/collections/{self.collection.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['items']), 1)
        self.assertEqual(response.data['items'][0]['title'], self.item.title)

    def test_create_collection(self):
        response = self.client.post('/api/collections/', {'name': 'New Collection'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Collection.objects.filter(name='New Collection').exists())
