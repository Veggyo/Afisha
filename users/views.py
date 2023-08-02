from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .serializers import *
from rest_framework import status
from users.models import *


@api_view(['POST'])
def registration_api_view(request):
    if request.method == "POST":

        serializer = RegistrationValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.create_user(username=username, password=password, is_active=False)

        confirming_code = ConfirmToken(user=user)
        confirming_code.code = confirming_code.generate_code()
        confirming_code.save()

        return Response(status=status.HTTP_201_CREATED, data={'user_is': user.username})


@api_view(['POST'])
def confirming_api_view(request):
    if request.method == 'POST':
        serializer = ConfirmTokenSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data['code']
            try:
                confirming_code = ConfirmToken.objects.get(code=code, is_using=False)
                user = confirming_code.user
                user.is_active = True
                user.save()

                confirming_code.is_using = True
                confirming_code.save()
                return Response(status=status.HTTP_201_CREATED, data={'message': 'User confirmed successfully!'})
            except ConfirmToken.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Invalid confirmation code'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
