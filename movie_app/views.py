from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['GET', 'POST'])
def directors_list_api_view(request):
    if request.method == 'GET':
        search = request.query_params.get('search', '')
        directors = Director.objects.filter(name__icontains=search).prefetch_related('movies')
        data = DirectorSerializer(instance=directors, many=True).data
        return Response(data)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(director).data)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={"message": "Объект режиссера не существует"}, status=404)
    if request.method == 'GET':
        data = DirectorSerializer(instance=director, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data)
    else:
        director.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all().prefetch_related('reviews')
        data = MovieSerializer(instance=movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_ids = request.data.get('director')
        movie = Movie.objects.create(title=title, description=description, duration=duration)
        movie.director.set(director_ids)
        movie.save()
        return Response(data=MovieSerializer(movie).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={"message": "Объект фильма не существует"}, status=404)
    if request.method == 'GET':
        data = MovieSerializer(instance=movie, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        director_ids = request.data.get('director')
        movie.director.set(director_ids)
        movie.save()
        return Response(data=MovieSerializer(movie).data)
    else:
        movie.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all().prefetch_related('movie')
        data = ReviewSerializer(instance=reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = request.data.get('text')
        movie_id = request.data.get('movie')  # Предполагается, что предоставляется один идентификатор фильма
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, stars=stars)
        review.movie.set([movie_id])
        review.save()
        return Response(data=ReviewSerializer(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={"message": "Review object doesn't exist"}, status=204)

    if request.method == 'GET':
        data = ReviewSerializer(instance=review, many=False).data
        return Response(data=data)

    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review.text = request.data.get('text')
        review.movie.set(request.data.get('movie'))
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data)

    else:
        review.delete()
        return Response(status=204)


@api_view(['GET'])
def movie_reviews(request):
    movies = Movie.objects.all().prefetch_related('reviews')
    data = MovieReviewSerializer(instance=movies, many=True).data
    return Response(data)
