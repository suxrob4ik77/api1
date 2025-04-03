

from django.urls import path
from .views import *

urlpatterns = [
    #   path('ism_api/',ism_api,name='ism_api'),
    # path('movies/', movie_api, name='movie-list'),
    path('movie_detail/<slug:slug>/', movie_detail, name='movie_detail'),
    path("movies/", movie_list_create, name="movie-list-create"),
]
