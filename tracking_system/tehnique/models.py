from django.db import models
from system_track.models import Building


# Create your models here.

class Tehnique(models.Model):
    name = models.CharField(max_length=200, unique=True)
    inventory_number = models.CharField(max_length=255, unique=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='tehniques', blank=True, null=True)

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

    def __str__(self):
        return f'{self.name}'
