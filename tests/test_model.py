from django.test import TestCase, SimpleTestCase
from collection.views import *

class MovieModelTest(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            uuid='57baf4f4-c9ef-4197-9e4f-acf04eae5b4d',
            title='Foo bar',
            description='A description of the test movie.',
            genres='Action'
        )

    def test_movie_title(self):
        self.assertEqual(self.movie.title, 'Foo bar')

    def test_movie_description(self):
        self.assertEqual(self.movie.description, 'A description of the test movie.')

    def test_movie_genres(self):
        self.assertEqual(self.movie.genres, 'Action')


class CollectionModelTest(TestCase):

    def setUp(self):
        self.movie = Collection.objects.create(
            uuid='57baf4f4-c9ef-4197-9e4f-acf04eae5b4d',
            title='John Doe',
            description='A description of the test collection.',
        )

    def test_movie_title(self):
        self.assertEqual(self.movie.title, 'John Doe')

    def test_movie_description(self):
        self.assertEqual(self.movie.description, 'A description of the test collection.')

