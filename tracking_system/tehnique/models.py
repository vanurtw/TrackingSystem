from django.db import models


# Create your models here.

class Tehnique(models.Model):
    name = models.CharField(max_length=200)
    inventory_number = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'
