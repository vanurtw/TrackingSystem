from django.db import models
from system_track.models import Building


# Create your models here.


class Tehnique(models.Model):
    CHOICES = [
        ('A', 'Техника находится в здании'),
        ('B', 'Техника передана из здания в здание, и ожидает фактического приема'),
        ('C', 'Техника принята в здании')
    ]
    name = models.CharField(max_length=200, unique=True)
    inventory_number = models.CharField(max_length=255, unique=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='tehniques', blank=True, null=True)
    parent_building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='parent_tichnique', blank=True,
                                        null=True)
    status = models.CharField(max_length=10, choices=CHOICES, default='A')
    date_crate = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

    def __str__(self):
        return f'{self.name}'
