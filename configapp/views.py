#
# from rest_framework import status, response
# from  rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from .serializers import *
#
# @api_view(["GET","POST"])
# def movie_api(request):
#     if request.method=="GET":
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)
#     if request.method=="POST":
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data,status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['PUT', 'PATCH', 'DELETE'])
# def movie_detail(request, slug):
#     try:
#         movie = Movie.objects.get(slug=slug)
#         response = {"succes": True}
#     except Exception as e:
#         response["error"] = e
#         return Response(data=response, status=status.HTTP_417_EXPECTATION_FAILED)
#     if request.method == 'GET':
#         response['data'] = movie
#         serializers = MovieSerializer(movie)
#         response['data'] = serializers
#         return Response(data=response, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializers = MovieSerializer(movie, data=request.data)
#
#         if serializers.is_valid(raise_exception=True):
#             serializers.save()
#             response['data'] = serializers
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         return Response(data=serializers.errors,status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer

@api_view(["GET", "POST"])
def movie_api(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def movie_detail(request, slug):
    try:
        movie = Movie.objects.get(slug=slug)
    except Movie.DoesNotExist:
        return Response({"success": False, "error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method in ["PUT", "PATCH"]:
        serializer = MovieSerializer(movie, data=request.data, partial=(request.method == "PATCH"))
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        movie.delete()
        return Response({"success": True, "message": "Movie deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

