from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Genre, Review, Movie


User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'content', 'vote', 'movie', 'updated_at', 'created_at')
        read_only_fields = ('movie', )


class MovieSerializer(serializers.ModelSerializer):
    
    class UserSerialzer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model=Genre
            exclude = ['id']

    genres = GenreSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    like_users = UserSerialzer(read_only=True, many=True)
    looked_users = UserSerialzer(read_only=True, many=True)


    class Meta:
        model = Movie
        fields=(
        'pk', 
        'title', 
        'release_date', 
        'popularity', 
        'vote_count', 
        'vote_average', 
        'overview', 
        'poster_path', 
        'runtime', 
        'genres',  
        'reviews',
        'like_users',
        'looked_users',
        'src',
        )


class MovieListSerializer(serializers.ModelSerializer):
    
    reviews_count = serializers.IntegerField()

    class Meta:
        model = Movie
        fields=(
        'pk', 
        'title', 
        'release_date', 
        'popularity', 
        'vote_count', 
        'vote_average', 
        'overview', 
        'poster_path', 
        'runtime', 
        'genres', 
        'reviews_count',
        )


class MovieRecommendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields=(
        'pk', 
        'title', 
        'release_date', 
        'popularity', 
        'vote_count', 
        'vote_average', 
        'overview', 
        'poster_path', 
        'runtime', 
        'genres', 
        )