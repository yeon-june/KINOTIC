import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kinotic.settings")

import django
django.setup()

import requests
import json
from movies.models import Movie



# if __name__ == '__main__':
#     for j in range(45, 60):
#         Base_URL = 'https://api.themoviedb.org/3'
#         path = '/movie/popular'
#         params = {
#             'api_key' : 'e73cf3371bb27a97420ed90450a7bbce',
#             'language' : 'ko-KR',
#             'page' : j,
#         }

#         response = requests.get(Base_URL+path, params = params)
#         movie_popular = response.json()

#         for movie in movie_popular['results']:
#             movie_title = movie['title']
#             movie_releasedate = movie['release_date']
#             movie_voteaverage = movie['vote_average']
#             movie_votecount = movie['vote_count']
#             movie_posterpath = movie['poster_path']
#             movie_popularity = int(movie['popularity']*1000)
#             movie_id = movie['id']
#             movie_overview = movie['overview']
#             movie_genre = movie['genre_ids']

#             path=f'/movie/{movie_id}'
#             params = {
#             'api_key' : 'e73cf3371bb27a97420ed90450a7bbce',
#             'language' : 'ko-KR',
#             }
#             response2 = requests.get(Base_URL+path, params = params)
#             movie_detail = response2.json()
#             movie_runtime = movie_detail['runtime']

#             movie = Movie.objects.create(
#                 title = movie_title,
#                 release_date = movie_releasedate,
#                 popularity = movie_popularity,
#                 vote_count = movie_votecount,
#                 vote_average = movie_voteaverage,
#                 overview = movie_overview,
#                 poster_path = movie_posterpath,
#                 runtime = movie_runtime,
#             )
#             for i in movie_genre:
#                 movie.genres.add(i)

# movie = Movie.objects.all()[96]

# title = movie.title
# params = {
#     'key': 'AIzaSyA0ZPLyvp_6Eas5z78e0M9mJXEAxOSsBog',
#     'part': 'snippet',
#     'q': title + ' official trailer',
#     'type': 'video',
#     'maxResults': '1'
# }
# URL = "https://www.googleapis.com/youtube/v3/search"
# response = requests.get(URL, params=params)
# src = 'https://www.youtube.com/embed/' + \
#     json.loads(response.text)['items'][0]['id']['videoId']
# data = {
#     'src': src+'?autoplay=1&mute=0&enablejsapi=1&controls=0&disablekb=1&modestbranding=1&rel=0&showinfo=0'
# }
# movie.src = data['src']
# movie.save()


# m = 15814
# C = 6.6366635249764325

# if __name__ == '__main__':
#     for j in range(1, 100):
#         Base_URL = 'https://api.themoviedb.org/3'
#         path = '/movie/popular'
#         params = {
#             'api_key' : 'e73cf3371bb27a97420ed90450a7bbce',
#             'language' : 'ko-KR',
#             'page' : j,
#         }

#         response = requests.get(Base_URL+path, params = params)
#         movie_popular = response.json()

#         for movie in movie_popular['results']:
#             movie_title = movie['title']
#             new_movie = Movie.objects.filter(title=movie_title)
#             movie_original_title = movie['original_title']
#             for i in new_movie:
#                 i.original_title = movie_original_title
#                 i.save()

m = 15814
C = 6.6366635249764325
movies = Movie.objects.all()
for movie in movies:
    v = movie.vote_count
    R = movie.vote_average
    ans = ((v/(v+m))*R) + ((m/(v+m))*C)
    movie.wr = ans
    movie.save()

