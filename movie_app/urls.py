from movie_app import views
from django.urls import path

urlpatterns = [
    # for CBV urls
    path('', views.MoviesListApiView.as_view()),
    path('directors/', views.DirectorsListApiView.as_view()),
    path('directors/<int:id>', views.DirectorsDetailApiView.as_view()),
    path('movies/', views.MoviesListApiView.as_view()),
    path('movies/<int:id>', views.MovieDetailApiView.as_view()),
    path('reviews/', views.ReviewsListApiView.as_view()),
    path('reviews/<int:id>', views.ReviewsDetailApiView.as_view())

    # for FBV urls
    # path('api/v1/directors/', views.directors_list_api_view),
    # path('<int:id>/', views.director_detail),
    # path('api/v1/movies/', views.movie_list_api_view),
    # path('<int:id>/', views.movie_detail),
    # path('api/v1/reviews/', views.reviews_list_api_view),
    # path('<int:id>/', views.review_detail),
    # path('api/v1/movies/reviews/', views.movie_reviews)
]
