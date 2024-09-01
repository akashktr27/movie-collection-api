from rest_framework.test import APITestCase, APIClient
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from collection.views import *
from rest_framework_simplejwt.tokens import RefreshToken

class MovieAPIViewTests(APITestCase):
    movie_url = reverse('movies')

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='some-strong-password')
        # self.token = Token.objects.create(user=self.user)
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)

    def tearDown(self):
        pass

    def test_get_movie_authenticated(self):
        # need to be fixed
        response = self.client.get(self.movie_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_movie_unauthenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.movie_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_movie_unauthenticated(self):
        pass