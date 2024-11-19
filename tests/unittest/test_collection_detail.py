from django.test import TestCase, SimpleTestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from collection.models import Movie, Collection
from django.urls import reverse, resolve
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from collection.views import *
from rest_framework_simplejwt.tokens import RefreshToken

class CollectionDetailViewTests(APITestCase):
    collections_url = reverse("collection")

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='some-strong-password')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)

        # saving collection
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
        response_post = self.client.post(self.collections_url, data, format='json')


    def test_get_collection_authenticated(self):
        response = self.client.get(self.collections_url)
        uuid = response.json().get('data').get('collections')[0].get('uuid')
        collection_url = reverse("collection-detail", args=[uuid])
        resp = self.client.get(collection_url)
        self.assertEqual(resp.status_code, 200)

    def test_get_collection_unauthenticated(self):
        response = self.client.get(self.collections_url)
        uuid = response.json().get('data').get('collections')[0].get('uuid')
        collection_url = reverse("collection-detail", args=[uuid])
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(collection_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)