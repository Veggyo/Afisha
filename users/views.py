from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .serializers import AuthorizationValidateSerializer, RegistrationValidateSerializer
from django.contrib.auth.models import User
from rest_framework import status


@api_view(['POST'])
def registration_api_view(request):
    if request.method == "POST":

        serializer = RegistrationValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.create_user(username=username, password=password, is_active=False)
        return Response(status=status.HTTP_201_CREATED, data={'user_is': user.username})


@api_view(['POST'])
def authorization_api_view(request):
    serializer = AuthorizationValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = authenticate(username=username, password=password, is_active=True)

    if user is not None:
        token_, create = Token.objects.get_or_create(user=user)
        return Response(data={'key': token_.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED, data={'message': 'user does not found'})
