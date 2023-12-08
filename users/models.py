from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    club_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

