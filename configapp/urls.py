#
# from django.urls import path
# from .views import *
# urlpatterns = [
#     path('movie_api/',movie_api),
#     path('movie_detail/<slug:slug>/',movie_detail)
# ]


from django.urls import path
from .views import movie_api, movie_detail

urlpatterns = [
    path('movies/', movie_api, name='movie-list'),  # Barcha filmlar + yangi film qo‘shish
    path('movies/<slug:slug>/', movie_detail, name='movie-detail'),  # Bitta filmga CRUD amallari
]
