from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Review
from community.models import Article

class ProfileSerializer(serializers.ModelSerializer):


    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_path')


    class ArticleSerializer(serializers.ModelSerializer):

        class Meta:
            model = Article
            fields = ('pk', 'title', 'content', 'created_at')


    class ReviewSerializer(serializers.ModelSerializer):

        class MovieSerializer2(serializers.ModelSerializer):
            
            class Meta:
                model = Movie
                fields = ('pk', 'title')

        movie = MovieSerializer2(read_only = True)

        class Meta:
            model = Review
            fields = ('pk', 'content', 'movie', 'vote', 'created_at')


    class ProfileSerializer2(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')


    followers = ProfileSerializer2(many=True)
    followings = ProfileSerializer2(many=True)        
    articles = ArticleSerializer(many=True, read_only=True)
    reviews_list = ReviewSerializer(many=True, read_only=True)
    like_movie = MovieSerializer(many=True)
    looked = MovieSerializer(many=True)


    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_movie', 'looked', 'profile_image', 'followings', 'followers', 'articles', 'reviews_list')

