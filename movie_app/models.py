from django.db import models
from django.db.models import Avg
from rest_framework.response import Response


class Director(models.Model):
    name = models.CharField(max_length=89)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    @property
    def rating(self, request):
        average_rating = Review.objects.all().aggregate(Avg('rating'))
        return Response({'average_rating': average_rating['rating__avg']})

    def __str__(self):
        return self.title


CHOICES = (
    ('1', '*'),
    ('2', '**'),
    ('3', '***'),
    ('4', '****'),
    ('5', '*****')
)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField(default=5, choices=CHOICES)

    def __str__(self):
        return self.text
