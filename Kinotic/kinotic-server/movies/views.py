from datetime import datetime
from .models import Movie, Review
from django.db.models import Count
from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer, MovieRecommendSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from bs4 import BeautifulSoup
from django.http import JsonResponse
import requests
import random


# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.annotate(
        reviews_count = Count('reviews', distinct=True)
    )
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    

@api_view(['POST'])
def look_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.looked_users.filter(pk=user.pk).exists():
        movie.looked_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.looked_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def create_review(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)

        # 기존 serializer 가 return 되면, 단일 comment 만 응답으로 받게됨.
        # 사용자가 댓글을 입력하는 사이에 업데이트된 comment 확인 불가 => 업데이트된 전체 목록 return 
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def review_update_or_delete(request, movie_pk, reviews_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=reviews_pk)

    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_comment()


# 날씨 기반 영화 추천
@api_view(['GET'])
def weather_recommend(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?lat=37.30101111&lon=127.0122222&appid=7e625d2f562b1014869529981bd7ee18'
    # request the API data and convert the JSON to Python data types
    city_weather = requests.get(url).json()
    # 필요한 정보들만 가져오기

    weather = {
        'main': city_weather['weather'][0]['main'],
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    # 일단 딕셔너리로 날씨에 장르들 하나씩을 선택 하도록 함(더 좋은 방법 있으면 그걸로 구현)
    lst = {'clear sky': 28, 'few clouds': 12, 'overcast clouds': 16, 'drizzle': 35, 'rain': 53, 'light rain': 9648, 'moderate rain': 80,'shower rain': 99, 'thunderstorm': 18,
           'snow': 10751, 'mist': 14, 'broken clouds': 27, 'scattered clouds': 10749}
    if weather['description'] not in lst:
        genre = 28
    else:
        genre = lst[weather['description']]
    # 장르와 같은 영화 정보들 가지고오기

    movie_list = Movie.objects.filter(genres=genre)
    choice_movies = set()
    if len(movie_list) >= 20:
        while len(choice_movies) < 20:
            movie = random.choice(movie_list)
            choice_movies.add(movie)
    else:
        for movie in movie_list:
            choice_movies.add(movie)
        movie_list = Movie.objects.order_by('-wr')[:100]
        while len(choice_movies) < 20:
            movie = random.choice(movie_list)
            choice_movies.add(movie)

    choice_movies = list(choice_movies)
    serializers = MovieRecommendSerializer(choice_movies, many=True)

    return Response(serializers.data, status.HTTP_200_OK)


# 유저 좋아요한 영화 장르 기반 가중치 부여 후 뽑기
@api_view(['GET'])
def likemovie_recommend(request):
    user = request.user
    choice_movies = set()

    # 유저가 좋아요 한 영화 장르에서 추천
    user_likemovies = user.like_movie.all()
    if user_likemovies:

        # 장르별 영화리스트
        movies = get_list_or_404(Movie)
        movieList = {}
        for movie in movies:
            for genre in movie.genres.all():
                if genre in movieList:
                    movieList[genre].append(movie)
                else:
                    movieList[genre] = []

        like_list = []
        for user_likemovie in user_likemovies:
            for likegenres in user_likemovie.genres.all():
                like_list.append(likegenres)
        
        # 20개 추천
        idx = 0
        while idx < 20:
            cnt = 0
            for genre in like_list:
                if movieList[genre]:
                    pass
                else:
                    cnt += 1
            if cnt == len(like_list):
                break
            
            randomgenre = random.choice(like_list)
            if movieList[randomgenre]:
                randommovie = random.choice(movieList[randomgenre])
                if randommovie in user.looked.all():
                    pass
                else:
                    choice_movies.add(randommovie)
                    idx += 1
            
        # 부족한 경우
        movie_list = Movie.objects.order_by('-wr')[:100]
        while len(choice_movies) < 20:
            movie = random.choice(movie_list)
            if movie not in request.user.looked.all():
                choice_movies.add(movie)

    # 좋아하는 영화가 없는 경우    
    else:
        movie_list = Movie.objects.order_by('-wr')[:100]
        choice_movies = []
        while len(choice_movies) < 20:
            movie = random.choice(movie_list)
            if movie not in choice_movies and movie not in user.looked.all():
                choice_movies.append(movie)
        
        serializers = MovieRecommendSerializer(choice_movies, many=True)

        return Response(serializers.data, status.HTTP_200_OK)
    
    choice_movies = list(choice_movies)
    serializers = MovieRecommendSerializer(choice_movies, many=True)

    return Response(serializers.data, status.HTTP_200_OK)


# 유저 팔로우한 사람 좋아요 목록 기반
@api_view(['GET'])
def following_recommend(request):
    user = request.user
    choice_movies = set()
    user_followings = user.followings.all()
    if user_followings:
        for following in user_followings:
            following_likemovies = following.like_movie.all()
            if following_likemovies:
                for following_likemovie in following_likemovies:
                    if following_likemovie not in user.looked.all():
                        if len(choice_movies) < 20:
                            choice_movies.add(following_likemovie)
                        else:
                            break
            elif len(choice_movies) >= 20:
                break
            else:
                pass
    
    # 팔로잉한 사람이 없는 경우
    else:
        movie_list = Movie.objects.order_by('-wr')[:100]
        choice_movies = []
        while len(choice_movies) < 20:
            movie = random.choice(movie_list)
            if movie not in choice_movies and movie not in user.looked.all():
                choice_movies.append(movie)
        
        serializers = MovieRecommendSerializer(choice_movies, many=True)

        return Response(serializers.data, status.HTTP_200_OK)
    
    # 부족한 경우
    if len(choice_movies) < 20:
        if user_followings:
            for following in user_followings:
                following_lookedmovies = following.looked.all()
                if following_lookedmovies:
                    for following_lookedmovie in following_lookedmovies:
                        if following_lookedmovie not in user.looked.all():
                            if len(choice_movies) < 20:
                                choice_movies.add(following_lookedmovie)
                            else:
                                break
                elif len(choice_movies) >= 20:
                    break
                else:
                    pass
    
    if len(choice_movies) < 20:
        movie_list = Movie.objects.order_by('-wr')[:100]
        while len(choice_movies) < 20:
            movie = random.choice(movie_list)
            if movie not in choice_movies and movie not in user.looked.all():
                choice_movies.add(movie)
    
    choice_movies = list(choice_movies)
    serializers = MovieRecommendSerializer(choice_movies[:20], many=True)

    return Response(serializers.data, status.HTTP_200_OK)


@api_view(['GET'])
def basic_recommend(request):
    movie_list = Movie.objects.order_by('-wr')[:100]
    choice_movies = []
    while len(choice_movies) < 20:
        movie = random.choice(movie_list)
        if movie not in choice_movies:
            choice_movies.append(movie)
    
    serializers = MovieRecommendSerializer(choice_movies, many=True)

    return Response(serializers.data, status.HTTP_200_OK)


@api_view(['GET'])
def boxoffice_movie(request):
    response = {
        'title' : [],
        'image' : [],
    }
    headers = {'User-Agent':'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/101.0.4951.67 safari/537.36'}
    data = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=박스오피스', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    movies = soup.select('#main_pack > div.sc_new.cs_common_module.case_list.color_1._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div.mflick > div._panel_popular._tab_content > div.list_image_info.type_pure_top > div > ul:nth-child(1) > li > a > div')

    for movie in movies:
        movie_img = movie.select_one('div.thumb > img')['src']
        movie_title = movie.select_one('div.title_box > strong')
        response['title'].append(movie_title.text)
        response['image'].append(movie_img)
    response['title'] = response['title'][:10]
    response['image'] = response['image'][:10]
    
    return JsonResponse(response)


@api_view(['GET'])
def movie_search(request, search):
    origin_movies = list(Movie.objects.filter(title__contains=search))
    local_movies = list(Movie.objects.filter(original_title__contains=search))
    
    origin_movies = list(set(origin_movies + local_movies))

    serializers = MovieSerializer(origin_movies, many=True)
    
    return Response(serializers.data, status.HTTP_200_OK)


@api_view(['GET'])
def range_movie(request,rangetype):
    if rangetype == '1':
        today = datetime.today()
        movies = Movie.objects.filter(release_date__gt=f'{today.date()}').order_by('release_date')
        serializers = MovieRecommendSerializer(movies, many=True)

        return Response(serializers.data, status.HTTP_200_OK)

    elif rangetype == '2':
        today = datetime.today()
        movies = Movie.objects.filter(release_date__lte=f'{today.date()}').order_by('-vote_average')
        serializers = MovieRecommendSerializer(movies, many=True)

        return Response(serializers.data, status.HTTP_200_OK)

    elif rangetype == '3':
        today = datetime.today()
        movies = Movie.objects.filter(release_date__lte=f'{today.date()}', vote_average__gt=4.0).order_by('vote_average')
        serializers = MovieRecommendSerializer(movies, many=True)

        return Response(serializers.data, status.HTTP_200_OK)

    elif rangetype == '4':
        today = datetime.today()
        movies = Movie.objects.filter(release_date__lte=f'{today.date()}').order_by('-vote_count')
        serializers = MovieRecommendSerializer(movies, many=True)

        return Response(serializers.data, status.HTTP_200_OK)

    elif rangetype == '5':
        today = datetime.today()
        movies = Movie.objects.filter(release_date__lte=f'{today.date()}').order_by('-release_date')
        serializers = MovieRecommendSerializer(movies, many=True)

        return Response(serializers.data, status.HTTP_200_OK)

    elif rangetype == '6':
        today = datetime.today()
        movies = Movie.objects.filter(release_date__lte=f'{today.date()}').order_by('release_date')
        serializers = MovieRecommendSerializer(movies, many=True)

        return Response(serializers.data, status.HTTP_200_OK) 

    elif rangetype == '7':
        today = datetime.today()
        movies = Movie.objects.filter(release_date__lte=f'{today.date()}').order_by('-runtime')
        serializers = MovieRecommendSerializer(movies, many=True)

        return Response(serializers.data, status.HTTP_200_OK)

    elif rangetype == '8':
        today = datetime.today()
        movies = Movie.objects.filter(release_date__lte=f'{today.date()}').order_by('runtime')
        serializers = MovieRecommendSerializer(movies, many=True)

        return Response(serializers.data, status.HTTP_200_OK)

    else:
        today = datetime.today()
        movies = Movie.objects.filter(release_date__lte=f'{today.date()}').order_by('title')
        serializers = MovieRecommendSerializer(movies, many=True)

        return Response(serializers.data, status.HTTP_200_OK)   

