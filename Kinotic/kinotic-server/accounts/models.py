from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    like_movie = models.ManyToManyField(Movie, related_name='like_users')
    looked = models.ManyToManyField(Movie, related_name='looked_users')
    profile_image = models.ImageField(default='../static/default.jpg')