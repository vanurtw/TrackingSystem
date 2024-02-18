from django.db import models


# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120)
    data_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Technique(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170)
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
