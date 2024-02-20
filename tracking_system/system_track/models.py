from django.db import models


# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120)
    data_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


