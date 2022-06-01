from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(blank=True)
    popularity = models.IntegerField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.TextField()
    runtime = models.IntegerField()
    genres = models.ManyToManyField('Genre', related_name='genress')
    src = models.TextField(blank=True)
    original_title = models.TextField(blank=True)
    wr = models.FloatField()


class Review(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews_list')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    vote = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])