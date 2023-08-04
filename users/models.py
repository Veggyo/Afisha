from django.db import models
from django.contrib.auth.models import User
import random


class ConfirmToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    is_using = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_code()
        super().save(*args, **kwargs)

    def generate_code(self):
        return str(random.randint(100000, 999999))


class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=8)
    email = models.EmailField()
