from movie_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.movie_list_api_view),
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.directors_list_api_view),
    path('api/v1/directors/<int:id>/', views.director_detail),
    path('api/v1/movies/', views.movie_list_api_view),
    path('api/v1/movies/<int:id>/', views.movie_detail),
    path('api/v1/reviews/', views.reviews_list_api_view),
    path('api/v1/reviews/<int:id>/', views.review_detail),
    path('api/v1/movies/reviews/', views.movie_reviews)
]
