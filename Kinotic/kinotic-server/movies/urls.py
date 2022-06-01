from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/like/', views.like_movie),
    path('<int:movie_pk>/look/', views.look_movie),
    path('<int:movie_pk>/reviews/', views.create_review),
    path('<int:movie_pk>/reviews/<int:reviews_pk>/', views.review_update_or_delete),
    path('recommend/weather/', views.weather_recommend),
    path('recommend/likemovie/', views.likemovie_recommend),
    path('recommend/following/', views.following_recommend),
    path('recommend/basic/', views.basic_recommend),
    path('boxoffice/', views.boxoffice_movie),
    path('<search>/', views.movie_search),
    path('recommend/movieranges/<rangetype>/', views.range_movie),
]
