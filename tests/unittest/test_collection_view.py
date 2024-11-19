from rest_framework.test import APITestCase, APIClient
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from collection.views import *
from rest_framework_simplejwt.tokens import RefreshToken

class CollectionAPIViewTests(APITestCase):
    collection_url = reverse('collection')

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='some-strong-password')
        # self.token = Token.objects.create(user=self.user)
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)

    def tearDown(self):
        pass

    def test_get_collection_authenticated(self):
        # need to be fixed
        response = self.client.get(self.collection_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_collection_unauthenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.collection_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_collection_authenticated(self):
        data = {
            "title": "foo bar",
            "description": "some desc5",
            "movies": [
                {
                    "title": "john doe",
                    "description": "Bertram Oliphant West (also known as Bo West) wants to clear his unjustly smeared reputation. He joins the Foreign Legion, with Simpson his manservant in tow. But the fort they get posted to is full of eccentric legionnaires, and there is trouble brewing with the locals too. Unbeknown to Bo, his lady love has followed him in disguise...",
                    "genres": "Comedy",
                    "uuid": "123e4567-e89b-12d3-a456-426614174000"
                }
            ]
        }
        response = self.client.post(self.collection_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

