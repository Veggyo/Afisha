from rest_framework import serializers
from movie_app.models import *
from django.db.models import Avg


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director', ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'movie', 'stars']


class MovieReviewSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField(max_length=255)
    reviews = ReviewSerializer(many=True)

    def get_average_rating(self, obj):
        avg_rating = obj.reviews.aggregate(avg_rating=Avg('stars'))['avg_rating']
        return round(avg_rating, 2) if avg_rating is not None else 0.0
