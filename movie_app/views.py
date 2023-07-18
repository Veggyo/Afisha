from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .models import *
from .serializers import *


@api_view(['GET'])
def directors_list_api_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(instance=directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_detail(request, iid):
    try:
        director = Director.objects.get(id=iid)

    except Director.DoesNotExist:
        return Response(status=404)

    data = DirectorSerializer(instance=director, many=False)
    return Response(data=data)


@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(instance=movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail(request, iid):
    try:
        movie = Movie.objects.get(id=iid)

    except Movie.DoesNotExist:
        return Response(status=404)

    data = MovieSerializer(instance=movie, many=False)
    return Response(data=data)


@api_view(['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(instance=reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail(request, iid):
    try:
        review = Review.objects.get(id=iid)

    except Review.DoesNotExist:
        return Response(status=404)

    data = ReviewSerializer(instance=review, many=False)
    return Response(data=data)
