

from django.urls import path
from .views import movie_api, movie_detail

urlpatterns = [
    path('movies/', movie_api, name='movie-list'),
    path('movies/<slug:slug>/', movie_detail, name='movie-detail'),
]
