from django.db import models
from django.contrib.auth.models import AbstractUser
from system_track.models import Building


# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username
