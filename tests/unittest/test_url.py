from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from collection.views import *

class MovieURLTest(SimpleTestCase):

    def test_get_movie_isresolved(self):
        url = reverse('movies')
        self.assertEqual(resolve(url).func.view_class, MovieView)

class CollectionURLTest(SimpleTestCase):

    def test_get_movie_isresolved(self):
        url = reverse('collection')
        self.assertEqual(resolve(url).func.view_class, CollectionView)