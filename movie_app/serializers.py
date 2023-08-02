from rest_framework import serializers
from movie_app.models import *
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'movie')


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    def get_reviews(self, movie):
        return [i.stars for i in movie.reviews.all()]

    def get_rating(self, movie):
        return movie.rating


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=22)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=10, max_length=100)
    description = serializers.CharField(required=False, default='Empty text')
    duration = serializers.IntegerField(min_value=1)
    director = serializers.CharField(min_length=3)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255, min_length=2)
    movie_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1)

    def validate_category_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Category does not exists')
        return movie_id
