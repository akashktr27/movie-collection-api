from django.db import transaction
from rest_framework import serializers
from .models import *

class MovieModelSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['uuid', 'title', 'description', 'genres']


class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieModelSerialiser(many=True)  # Nested serializer to handle Movie validation

    def __init__(self, *args, **kwargs):
        # Extract the extra argument if provided
        self.detail = kwargs.pop('detail', False)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Collection
        fields = ['uuid', 'title', 'description', 'movies']

    def validate_movies(self, movies):
        for movie_data in movies:
            movie_serializer = MovieModelSerialiser(data=movie_data)
            if not movie_serializer.is_valid():

                raise serializers.ValidationError(movie_serializer.errors)
        return movies

    def validate(self, data):

        if Collection.objects.filter(title=data['title']).exists():
                raise serializers.ValidationError("A collection with this title already exists.")
        return data

    def create(self, validated_data):
        movies_data = validated_data.pop('movies')

        # Use a transaction to ensure atomicity
        with transaction.atomic():
            collection = Collection.objects.create(**validated_data)

            for movie_data in movies_data:
                movie_instance, created = Movie.objects.get_or_create(**movie_data)
                collection.movies.add(movie_instance)

        return collection

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if not self.detail:
            representation.pop('movies', None)
        return representation

    def update(self, instance, validated_data):
        movie_data = validated_data.pop('movies')
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        for movie in movie_data:
            movie_instance, created = Movie.objects.get_or_create(**movie)
            instance.movies.add(movie_instance)

        return instance