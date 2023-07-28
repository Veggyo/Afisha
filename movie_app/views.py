from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['GET', 'POST'])
def directors_list_api_view(request):
    if request.method == 'GET':
        # search = request.query_params.get('search', '')
        directors = Director.objects.prefetch_related('movies')
        data = DirectorSerializer(instance=directors, many=True).data
        return Response(data.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        directors = Director.objects.create(
            name=name
        )
        directors.save()
        return Response(data=DirectorSerializer(directors).data)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={"message: 'Director object doesn't exists'"}, status=404)
    if request.method == 'GET':
        data = DirectorSerializer(instance=director, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        return Response(data=DirectorSerializer(director).data)
    else:
        director.delete()
        return Response(status=404)


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all().prefetch_related('reviews')
        data = MovieSerializer(instance=movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        movies = Movie.objects.create(
            title=title, description=description, duration=duration
        )
        movies.director.set(director)
        movies.save()
        return Response(data=MovieSerializer(movies).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={"message: 'Movie object doesn't exists'"}, status=404)
    if request.method == 'GET':
        data = MovieSerializer(instance=movie, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director.set(request.data.get('director'))
        movie.save()
        return Response(data=MovieSerializer(movie).data)
    else:
        movie.delete()
        return Response(status=404)


@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        text = Review.objects.prefetch_related('text')
        data = ReviewSerializer(instance=text, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
        reviews = Director.objects.create(
            text=text, stars=stars
        )
        movie.save()
        return Response(data=ReviewSerializer(reviews).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={"message: 'Review object doesn't exists'"}, status=404)
    if request.method == 'GET':
        data = ReviewSerializer(instance=review, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie.set(request.data.get('movie'))
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data)
    else:
        review.delete()
        return Response(status=404)


@api_view(['GET'])
def movie_reviews(request):
    movies = Movie.objects.all().prefetch_related('reviews')
    data = MovieReviewSerializer(instance=movies, many=True).data
    return Response(data)
