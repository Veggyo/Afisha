from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class AuthorizationValidateSerializer(serializers.Serializer):
    pass


class RegistrationValidateSerializer(serializers.Serializer):
    def validate_username(self, username):
        try:
            User.objects.get(username=username)
            raise ValidationError('User already exists')
        except User.DoesNotExist:
            return username


class ConfirmTokenSerializer(serializers.Serializer):
    confirming_code = serializers.CharField(max_length=6)
