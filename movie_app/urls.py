from movie_app import views
from django.urls import path

urlpatterns = [
    path('', views.movie_list_api_view),
    path('api/v1/directors/', views.directors_list_api_view),
    path('<int:id>/', views.director_detail),
    path('api/v1/movies/', views.movie_list_api_view),
    path('<int:id>/', views.movie_detail),
    path('api/v1/reviews/', views.reviews_list_api_view),
    path('<int:id>/', views.review_detail),
    path('api/v1/movies/reviews/', views.movie_reviews)
]