from .views import *
from django.urls import path


urlpatterns = [
    path('authorization/', AuthorizationApiView.as_view()),
    path('registration/', RegistrationApiView.as_view()),
    path('confirm/', ConfirmApiView.as_view())
]
