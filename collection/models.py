from django.db import models
import uuid
# # Create your models here.
class Movie(models.Model):
    uuid = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    genres = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'movies'

class Collection(models.Model):
    title = models.CharField(max_length=100)
    uuid = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4)
    description = models.TextField()
    movies = models.ManyToManyField(Movie, related_name='collections')


    def __str__(self):
        return str(self.title)
